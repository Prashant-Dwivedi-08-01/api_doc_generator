import subprocess
from scrapper import create_updated_html

command = ['docgen' ,'build', '-i', 'test.postman_collection.json', '-o', 'api_doc.html']
subprocess.run(command)
create_updated_html()
