#!/usr/bin/python3
# starts a Flask web application
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    'returns hello hbnb for root index'
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    "returns 'hbnb' for /hbnb"
    return "HBNB"


@app.route('/c/<path:text>', strict_slashes=False)
def c_is_fun(text):
    "returns C and value of text, with _ as spaces"
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
