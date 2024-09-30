#!/usr/bin/python3

"""Function that returns an object (Python data structure)
represented by a JSON string."""

import json


def from_json_string(my_str):
    """
    Deserialize a JSON string into a Python object.

    Args:
        my_str (str): The JSON string to be deserialized.

    Returns:
        object: The deserialized Python object converted from the JSON string.
    """
    return json.loads(my_str)
