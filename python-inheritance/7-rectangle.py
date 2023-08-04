# -*- coding: utf-8 -*-
"""Module containing the Rectangle class.

This module defines the Rectangle class, which inherits from the BaseGeometry class.

Example:
    To use the Rectangle class, simply create an instance of it with positive integer values for width and height.

        r = Rectangle(3, 5)

Attributes:
    None

Todo:
    * Implement the area() method to compute the area of the rectangle.
    * Define the __str__ method to provide a string representation of the rectangle.

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

    def area(self):
        """Compute the area of the rectangle.

        Returns:
            int: The area of the rectangle.

        """
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
