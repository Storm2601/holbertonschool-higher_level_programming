#!/usr/bin/python3

"""Function that returns the JSON representation of an object (string)."""

import json


def to_json_string(my_obj):
    """
    Converts a Python object to its JSON string representation.

    Args:
        my_obj: The Python object to be converted to a JSON string.

    Returns:
        str: The JSON string representation of the input object.
    """
    return json.dumps(my_obj)
