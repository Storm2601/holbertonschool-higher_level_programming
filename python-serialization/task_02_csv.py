#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON format"""
    try:
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data_list = [row for row in csv_reader]

        json_data = json.dumps(data_list, indent=4)

        with open('data.json', mode='w') as json_file:
            json_file.write(json_data)

        return True

    except FileNotFoundError:
        return False
