"""
This script creates a simple Flask web application.

Usage:
    Run this script and access the web application in your browser or using curl.

Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the text variable
               (replace underscore _ symbols with a space)
    /python/(<text>): display “Python ”, followed by the value of the text variable
                      (replace underscore _ symbols with a space)
                      The default value of text is "is cool"
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display an HTML page only if n is an integer:
                          H1 tag: “Number: n” inside the BODY tag
    /number_odd_or_even/<n>: display an HTML page only if n is an integer:
                             H1 tag: “Number: n is even|odd” inside the BODY tag

Note:
    The web application listens on 0.0.0.0 and port 5000.
"""

from flask import Flask, escape, render_template

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

@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text):
    """
    This function defines the route '/python/' and '/python/<text>' which displays "Python " followed by the
    value of the text variable.

    Args:
        text (str): The text value specified in the URL. Default is "is cool".

    Returns:
        str: The string "Python " followed by the text value, with underscores replaced by spaces.
    """
    return "Python " + escape(text.replace("_", " "))

@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """
    This function defines the route '/number/<n>' which displays "<n> is a number" if n is an integer.

    Args:
        n (int): The integer value specified in the URL.

    Returns:
        str: The string "<n> is a number" if n is an integer.
    """
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    This function defines the route '/number_template/<n>' which displays an HTML page with the H1 tag
    "Number: n" inside the BODY tag.

    Args:
        n (int): The integer value specified in the URL.

    Returns:
        render_template: Renders the HTML template with the H1 tag displaying "Number: n".
    """
    return render_template("6-number_template.html", n=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    This function defines the route '/number_odd_or_even/<n>' which displays an HTML page with the H1 tag
    "Number: n is even|odd" inside the BODY tag.

    Args:
        n (int): The integer value specified in the URL.

    Returns:
        render_template: Renders the HTML template with the H1 tag displaying "Number: n is even|odd".
    """
    odd_or_even = "even" if n % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html", n=n, odd_or_even=odd_or_even)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
