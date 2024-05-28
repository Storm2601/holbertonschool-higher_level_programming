#!/usr/bin/python3
"""from_json_string"""


def from_json_string(my_str):
    """function that returns an object (Python data structure)"""
    import json
    return json.loads(my_str)
