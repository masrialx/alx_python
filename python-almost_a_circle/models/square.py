#!/usr/bin/python3
"""Module that contains the Square class"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class, inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)
