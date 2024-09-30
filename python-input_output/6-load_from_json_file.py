#!/usr/bin/python3

"""Load data from a JSON file and return the deserialized object."""

import json


def load_from_json_file(filename):
    """
    Load data from a JSON file and return the deserialized object.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        object: The deserialized object obtained from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
