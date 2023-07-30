#!/usr/bin/python3
"""
Module containing the BaseGeometry class.
"""


class BaseGeometry:
    """
    A class defining the base geometry.
    """

    def area(self):
        """
        Raises an Exception with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as an integer and raises appropriate exceptions if necessary.

        Args:
            name (str): The name of the value (used in the exception message).
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
