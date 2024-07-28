from flask import Flask, request, send_file
import os

app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download_file():
    filename = request.args.get('filename')

    # Vulnerable path traversal
    filepath = os.path.join(os.getcwd(), filename)

    # Check if file exists and send it
    if os.path.exists(filepath):
        return send_file(filepath, as_attachment=True)
    else:
        return "File not found", 404

if __name__ == '__main__':
    app.run(debug=True)