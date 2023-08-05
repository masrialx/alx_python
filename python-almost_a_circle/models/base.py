"""
models/base.py
Module containing the Base class that manages the id attribute for all future classes.
"""

class Base:
    """
    Base class to manage id attribute in all future classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.

        Args:
            id (int): The id attribute for the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
