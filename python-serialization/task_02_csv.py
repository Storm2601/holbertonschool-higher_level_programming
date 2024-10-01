#!/usr/bin/python3

"""
This script provides functionality to convert a CSV file
into a JSON file format using Python's built-in modules.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON format.

    Args:
        csv_filename (str): The path to the CSV file.

    Returns:
        bool: True if conversion is successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r') as csv_file:
            data_list = list(csv.DictReader(csv_file))

        with open('data.json', mode='w') as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
