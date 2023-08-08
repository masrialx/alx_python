#!/usr/bin/python3
"""Module containing the Rectangle class that inherits from Base."""
from models.base import Base

class Rectangle(Base):
    """
    Rectangle class that inherits from Base.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        __x (int): The x-coordinate of the rectangle.
        __y (int): The y-coordinate of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None, *args, **kwargs):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle.
            y (int): The y-coordinate of the rectangle.
            id (int): The id attribute for the instance.
            *args: Variable number of positional arguments.
            **kwargs: Variable number of keyword arguments.
        """
        super().__init__(id, *args, **kwargs)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # ... rest of the class remains the same
