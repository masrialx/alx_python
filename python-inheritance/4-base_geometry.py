# -*- coding: utf-8 -*-
"""Module containing the BaseGeometry class.

This module defines the BaseGeometry class, which serves as the base class for other geometrical shapes.

Example:
    To use the BaseGeometry class, simply create an instance of it.

        bg = BaseGeometry()
        print(bg)

Attributes:
    None

Todo:
    * Add additional methods and attributes to the BaseGeometry class.
    * Implement specific geometrical shapes based on BaseGeometry.

"""

class BaseGeometry:
    """An empty class defining the base geometry."""

    def area(self):
        """Compute the area of the geometrical shape.

        This method should be implemented in subclasses to calculate the area of specific geometrical shapes.

        Raises:
            Exception: Always raises an Exception with the message "area() is not implemented".

        """
        raise Exception("area() is not implemented")
