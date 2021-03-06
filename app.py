import os
from flask import Flask, render_template, request, redirect, send_file
from s3_functions.utils import download_file, list_files, upload_file

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = "file-management-bucket"


@app.route('/')
def entry_point():
    return 'Hello World'


@app.route('/storage')
def storage():
    contents = list_files('file-management-bucket')
    return render_template('storage.html', contents=contents)


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(UPLOAD_FOLDER, f.filename))
        upload_file(f"uploads/{f.filename}", BUCKET)

        return redirect("/storage")


@app.route("/download/<filename>", methods=['GET'])
def download(filename):
    if request.method == 'GET':
        output = download_file(filename, BUCKET)

        return send_file(output, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
