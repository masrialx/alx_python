# -*- coding: utf-8 -*-
"""Module containing the BaseGeometry class.

This module defines the BaseGeometry class, which is an empty class used as the base for other geometrical shapes.

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

    def __dir__(self):
        """Remove __init_subclass__ from the list of attributes."""
        attributes = dir(self.__class__)
        return [attr for attr in attributes if attr != '__init_subclass__']

