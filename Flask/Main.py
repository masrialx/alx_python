"""
0. Hello Flask!
A simple Flask web application that displays "Hello HBNB!" at the root URL.

This script starts a Flask web application that listens on 0.0.0.0 and port 5000.
The only route defined is '/', which displays the message "Hello HBNB!".
The option strict_slashes is set to False to allow for both '/hello' and '/hello/' routes.

Usage:
    Run this script using Python to start the Flask server.
    The application will be accessible at http://0.0.0.0:5000/.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL.
    
    Returns:
        str: A plain text message "Hello HBNB!".
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
