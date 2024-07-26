from flask import Flask, request, send_file, abort
import os

app = Flask(__name__)

UPLOAD_DIRECTORY = 'uploads'

@app.route('/download', methods=['GET'])
def download_file():
    filename = request.args.get('filename')

    # Securely sanitize and validate the filename
    safe_filename = os.path.basename(filename)
    filepath = os.path.join(UPLOAD_DIRECTORY, safe_filename)

    # Ensure the file is within the upload directory
    if os.path.commonprefix([UPLOAD_DIRECTORY, filepath]) == UPLOAD_DIRECTORY and os.path.exists(filepath):
        return send_file(filepath, as_attachment=True)
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
