#!/usr/bin/env python3

"""Module for serialization and deserialization of data."""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize data and save it to a JSON file.

    Args:
        data (dict): The data to serialize.
        filename (str): The name of the output file.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file.

    Args:
        filename (str): The name of the input file.

    Returns:
        dict: The deserialized data.
    """
    with open(filename, 'r') as file:
        return json.load(file)
