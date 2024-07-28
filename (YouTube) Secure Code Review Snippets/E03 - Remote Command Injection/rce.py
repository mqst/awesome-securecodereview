from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    host = request.args.get('host')

    # Vulnerable to command injection
    command = f"ping -c 1 {host}"
    result = os.popen(command).read()

    return f"<pre>{result}</pre>"

if __name__ == '__main__':
    app.run(debug=True)


# API calls
# Functionalities which invoke
    # system commands
    # system services

# Functions which execute system commands (Python):
    # os.popen()
    # os.system()
    # subprocess.Popen()
    # subprocess.run()
    # exec()