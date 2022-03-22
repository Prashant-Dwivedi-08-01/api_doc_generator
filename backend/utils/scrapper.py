from bs4 import BeautifulSoup

def create_updated_html(name):
    with open(f"./downloads/{name}.html", encoding = 'utf-8')  as f:
        soup = BeautifulSoup(f, 'html.parser')

        #find the all the panel. panel panel-default is the div that contains all the Collection folders one by one
        res = soup.find_all("div", class_="panel panel-default")

        #last div is variables
        variables = res[len(res)-1]

        #create new tag to write the variables 
        tag = soup.new_tag("div", class_ = "panel panel-default")
        data_inside_tag = BeautifulSoup(str(variables), 'html.parser')
        tag.append(data_inside_tag)

        #insert in the begining
        res[0].insert_before(tag)

        #remove the variables from the bottom
        variables.decompose()

        # Editing the heading and adding the logo
        collection_intro = soup.find("div", class_="collection-intro")
        collection_intro.h3.clear()

        #image
        img_tag = soup.new_tag("img", style="width:60px",src="./rest.png")
        collection_intro.h3.insert(0,img_tag)

        #heading
        doc_title = BeautifulSoup("API Documentation", 'html.parser')
        collection_intro.h3.insert(1, doc_title)

        # Remove the Footor
        footer = soup.footer
        footer.decompose()

        #save the file
        f = open(f"./downloads/{name}.html","wb")
        f.write(soup.prettify("utf-8"))