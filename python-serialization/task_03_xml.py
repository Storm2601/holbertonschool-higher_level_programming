#!/usr/bin/python3
"""Serialize a dictionary to XML format and write it to a file"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to XML format and write it to a file"""
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Convert all values to string

    tree = ET.ElementTree(root)

    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}

    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
