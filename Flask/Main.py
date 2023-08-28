"""Flask web application to display 'Hello HBNB!'.

The module creates a Flask application that handles 
requests to the route '/' to display a greeting.
"""

from flask import Flask

class HBNBFlaskApp(Flask):
  """Flask application class to display 'Hello HBNB!'.

  Handles requests to route '/' to display greeting.
  """

  def __init__(self, name):
    super().__init__(name)

    @self.route('/', strict_slashes=False)
    def display_greeting():
      """Display 'Hello HBNB!' greeting."""
      return 'Hello HBNB!'
      
if __name__ == '__main__':
  """Run the Flask web application."""
  app = HBNBFlaskApp(__name__)
  app.run(host='0.0.0.0', port=5000)