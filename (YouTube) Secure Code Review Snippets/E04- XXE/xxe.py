from flask import Flask, request
from lxml import etree

app = Flask(__name__)

@app.route('/parse', methods=['POST'])
def parse_xml():
    # Read XML data from the request
    xml_data = request.data

    # Parse XML data (vulnerable to XXE)
    try:
        parser = etree.XMLParser(resolve_entities=True)
        tree = etree.fromstring(xml_data, parser)
        return f"Parsed XML: {etree.tostring(tree, pretty_print=True).decode()}"
    except etree.XMLSyntaxError as e:
        return f"XML parsing error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)

# xml.etree.ElementTree
# 3rd party XML parsers