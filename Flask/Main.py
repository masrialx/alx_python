"""
Flask web application to display 'Hello HBNB!'.

The app handles requests to the route '/' to display a greeting.
"""

from flask import Flask

class HBNBFlaskApp(Flask):
    """Flask application class for 'Hello HBNB!'.

    Handles requests to route '/' to display greeting.
    """
    
    def __init__(self, name):
        super().__init__(name)
        
        @self.route('/', strict_slashes=False)
        def display_greeting():
            """Display 'Hello HBNB!' greeting.

            Returns the string 'Hello HBNB!'.
            """
            return 'Hello HBNB!'
            
if __name__ == '__main__':
    """Runs the Flask web application.

    Creates a Flask app instance and runs it on host '0.0.0.0' port 5000.
    """
    app = HBNBFlaskApp(__name__)
    app.run(host='0.0.0.0', port=5000)