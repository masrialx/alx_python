"""
This script creates a simple Flask web application.

Usage:
    Run this script and access the web application in your browser or using curl.

Routes:
    /: Displays "Hello HBNB!"
    /hbnb: Displays "HBNB"
    /c/<text>: Displays "C " followed by the value of the text variable
               (replace underscore _ symbols with a space)

Note:
    The web application listens on 0.0.0.0 and port 5000.
"""

from flask import Flask, escape

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """
    This function defines the route '/' which displays "Hello HBNB!".

    Returns:
        str: The string "Hello HBNB!" which is displayed in the browser.
    """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    This function defines the route '/hbnb' which displays "HBNB".

    Returns:
        str: The string "HBNB" which is displayed in the browser.
    """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """
    This function defines the route '/c/<text>' which displays "C " followed by the value of the text variable.

    Args:
        text (str): The text value specified in the URL.

    Returns:
        str: The string "C " followed by the text value, with underscores replaced by spaces.
    """
    return "C " + escape(text.replace("_", " "))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
