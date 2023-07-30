#!/usr/bin/python3
"""Module to check if an object is an instance of a specified class."""

def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of the class, False otherwise.
    """
    return type(obj) is a_class