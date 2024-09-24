#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance
of a class that inherited (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Parameters:
    obj: The object to check.
    a_class: The class to compare against.

    Returns:
    bool: True if obj is an instance of a class that inherited from a_class;
          otherwise, False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
