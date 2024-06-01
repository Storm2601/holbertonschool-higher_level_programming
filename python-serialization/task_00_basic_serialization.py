#!/usr/bin/env python3
"""Serialization and Deserialization of data"""


def serialize_and_save_to_file(data, filename):
    import json
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    import json
    with open(filename, 'r') as file:
        return json.load(file)
