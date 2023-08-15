#!flask/bin/python
from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/')
def index():
    return """
    <html>
        <head>
            <title>Python Script Generator</title>
        </head>
        <body>
            <h1>Python Script Generator</h1>
            <form action="generate_script" method="POST">
                Input Text: <input type="text" name="input_text"><br>
                <input type="submit" value="Generate Script">
            </form>
        </body>
    </html>
    """


@app.route('/generate_script', methods=['POST'])
def generate_script():
    input_text = request.form['input_text']
    python_code = generate_python(input_text)
    return Response(python_code, mimetype='text/plain', headers={'Content-Disposition':'attachment;filename=script.py'})


def generate_python(input_text):
    # write your Python code generation logic here based on the input text
    # return the generated Python code
    return "print('Hello World!')"


if __name__ == '__main__':
    app.run(debug=True)
