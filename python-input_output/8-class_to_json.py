#!/usr/bin/python3

"""Converts a Python object to a dictionary representation."""


def class_to_json(obj):
    """Convert a Python object to a dictionary representation.

    Args:
        obj: The object to be converted.

    Returns:
        dict: A dictionary representation of the object's attributes.
    """
    return obj.__dict__
