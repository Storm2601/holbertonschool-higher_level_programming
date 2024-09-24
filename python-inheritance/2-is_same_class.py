#!/usr/bin/python3
"""
This module defines a function that checks if an object is exactly
an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Parameters:
    obj: The object to check.
    a_class: The class to compare against.

    Returns:
    bool: True if obj is exactly an instance of a_class; otherwise, False.
    """
    return type(obj) is a_class
