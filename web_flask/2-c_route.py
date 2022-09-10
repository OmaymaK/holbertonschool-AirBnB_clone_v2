#!/usr/bin/python3
"""Flask Web App."""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Hello hbnb."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Hbnb."""
    return "HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def cisfun(text):
    """Cisfun."""
    text = text.replace('_', ' ')
    return f'C {text}'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
