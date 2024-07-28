from flask import Flask, request
from markupsafe import escape
import re

app = Flask(__name__)

@app.route('/checkout', methods=['GET'])
def checkout():
    backTo = request.args.get('backTo', '/')
    pattern = r'^(?:[a-zA-Z]+:|/)'

    # Forbidden keyword found, set to default value
    if re.match(pattern, backTo):
        backTo = '/'

    # The vulnerable part: no escaping here
    return f'''
        ...
        <a href="{backTo}">Back</a>
        ...
    '''

if __name__ == '__main__':
    app.run(debug=True, port=8080)
