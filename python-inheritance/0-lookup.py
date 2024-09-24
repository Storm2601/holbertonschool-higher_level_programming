#!/usr/bin/python3
""" Returns the list of available attributes and methods of an object."""


def lookup(obj):
    """
    Args:
        obj: The object to inspect.

Returns:
        A list containing the attributes and methods of the object.
    """
    return dir(obj)
