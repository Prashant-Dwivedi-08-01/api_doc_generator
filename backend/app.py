import os
from flask import Flask, flash, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from utils.common import response
from utils.scrapper import create_updated_html
import subprocess
from flask_cors import CORS
from flask import request

UPLOAD_FOLDER = './uploads'
DOWNLOAD_FOLDER = './downloads'

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.add_url_rule(
    "/uploads", endpoint="download_file", build_only=True
)


def create_html_doc(name):
    err = None
    try:
        input_file_name = name
        output_file_name = name.split(".")[0]
        command = ['docgen' ,'build', '-i', f'./uploads/{input_file_name}', '-o', f'./downloads/{output_file_name}.html']
        try:
            subprocess.run(command)
        except Exception as ex:
            err = "Error in Generating the HTML Doc"
            raise ex

        try:
            create_updated_html(output_file_name)
        except Exception as ex:
            err = "Error in Updating the Doc using the scrapper"
            raise ex

    except Exception as ex:
        print(f"Exception: {ex}. Error: {err}") 
        raise

@app.route('/downlaod')
def download_file():
    path = "./requirements.txt"
    return send_file(path, as_attachment=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    err = None
    result = ""
    filename = ""
    try:
        # check if the post request has the file part
        if 'collection' not in request.files:
            err = "Collection File is required"
            raise

        file = request.files["collection"]
            
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            err = 'No selected file'
            raise

        if file:
            filename = secure_filename(file.filename)

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            res = {
                "msg": "File Uploaded Successfully"
            }
            create_html_doc(filename)
            # return response(data=res)

            result = filename.split(".")[0] + ".html"
            # print(result)
            # uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
            return send_file(f"./downloads/{result}", as_attachment=True)

    except Exception as ex:
        print(f"Exception: {ex}. Error: {err}") 
        res = {
            "msg":err
        }
        return response(data=res, status=400)
    finally:
        for root, dirs, files in os.walk('./downloads'):
            if result in files:
                os.remove(f'./downloads/{result}')

        for root, dirs, files in os.walk('./uploads'):
            if filename in files:
                os.remove(f'./uploads/{filename}')

        print("Deleted both files successfully")


if __name__ == "__main__":
    app.run(debug=True)
