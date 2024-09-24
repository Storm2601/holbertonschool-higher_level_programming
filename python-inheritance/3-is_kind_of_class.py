#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance of,
or if the object is an instance of a class that inherited from,
a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if the object is an instance of
    a class that inherited from, the specified class.

    Parameters:
    obj: The object to check.
    a_class: The class to compare against.

    Returns:
    bool: True if obj is an instance of a_class or a subclass of a_class;
          otherwise, False.
    """
    return isinstance(obj, a_class)
