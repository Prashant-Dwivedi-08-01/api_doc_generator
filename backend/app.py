import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from utils.common import response
from utils.scrapper import create_updated_html
import subprocess

UPLOAD_FOLDER = './uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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

@app.route('/upload', methods=['POST'])
def upload_file():
    err = None
    try:
        # check if the post request has the file part
        file = request.files["collection"]
        if not file:
            err = "Collection File is required"
            raise
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
            return response(data=res)

    except Exception as ex:
        print(f"Exception: {ex}. Error: {err}") 
        res = {
            "msg":err
        }
        return response(data=res, status=400)

if __name__ == "__main__":
    app.run(debug=True)