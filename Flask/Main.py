"""
This script creates a simple Flask web application.

Usage:
    Run this script and access the web application in your browser or using curl.

Routes:
    /: Displays "Hello HBNB!"

Note:
    The web application listens on 0.0.0.0 and port 5000.
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """
    This function defines the route '/' which displays "Hello HBNB!".
    It uses the route() decorator from Flask to bind the function to the URL.

    Returns:
        str: The string "Hello HBNB!" which is displayed in the browser.
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
