#!/usr/bin/python3

"""Function to save a Python object to a file in JSON format."""

import json


def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to a file in JSON format.

    Args:
        my_obj: The Python object to be serialized and saved to the file.
        filename (str): The name of the file where the object will be saved.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
