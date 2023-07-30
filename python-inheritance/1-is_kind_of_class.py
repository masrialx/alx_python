#!/usr/bin/python3
"""Module to check if an object is an instance of a class or its subclass."""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or a subclass of, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of, or a subclass of, the class, False otherwise.
    """
    return isinstance(obj, a_class)
