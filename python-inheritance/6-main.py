# -*- coding: utf-8 -*-
"""Module containing the Rectangle class.

This module defines the Rectangle class, which inherits from the BaseGeometry class.

Example:
    To use the Rectangle class, simply create an instance of it with positive integer values for width and height.

        r = Rectangle(3, 5)

Attributes:
    None

Todo:
    * Implement additional methods or attributes as needed.
    * Add functionality for computing the area of a rectangle.

"""

from 5-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize the rectangle with given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If either width or height is not an integer.
            ValueError: If either width or height is not a positive integer.

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    # Implement additional methods for Rectangle as needed
