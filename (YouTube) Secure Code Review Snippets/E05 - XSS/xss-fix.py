from flask import Flask, request, render_template_string
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name', 'World')

    # Sanitize user input to prevent XSS
    safe_name = escape(name)

    return render_template_string('<h1>Hello, {}!</h1>'.format(safe_name))

if __name__ == '__main__':
    app.run(debug=True)
