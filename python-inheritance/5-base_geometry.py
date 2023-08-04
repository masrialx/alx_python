# -*- coding: utf-8 -*-
"""Module containing the BaseGeometry class.

This module defines the BaseGeometry class, which serves as the base class for other geometrical shapes.

Example:
    To use the BaseGeometry class, simply create an instance of it and call the `integer_validator` method.

        bg = BaseGeometry()
        bg.integer_validator("my_int", 12)

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

    def integer_validator(self, name, value):
        """Validate if a value is an integer and greater than 0.

        Args:
            name (str): The name of the variable to be validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
