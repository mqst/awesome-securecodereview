from flask import Flask, request, abort
import re
import subprocess

app = Flask(__name__)

def validate_host(host):
    # Simple regex to validate hostnames and IP addresses
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return pattern.match(host)

@app.route('/ping', methods=['GET'])
def ping():
    host = request.args.get('host')

    # Validate host parameter
    if not validate_host(host):
        abort(400, description="Invalid host")

    command = ["ping", "-c", "1", host]
    try:
        result = subprocess.check_output(command, universal_newlines=True)
        return f"<pre>{result}</pre>"
    except subprocess.CalledProcessError as e:
        return f"<pre>Error: {e}</pre>"

if __name__ == '__main__':
    app.run(debug=True)