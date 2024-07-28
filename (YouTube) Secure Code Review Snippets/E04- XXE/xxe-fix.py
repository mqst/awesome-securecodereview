from flask import Flask, request
from defusedxml.ElementTree import fromstring, tostring

app = Flask(__name__)

@app.route('/parse', methods=['POST'])
def parse_xml():
    xml_data = request.data

    # Safely parse XML data
    tree = fromstring(xml_data)

    return f"Parsed XML: {tostring(tree)}"

if __name__ == '__main__':
    app.run(debug=True)
