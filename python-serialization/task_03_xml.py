#!/usr/bin/python3

"""
Transform a dictionary into an XML structure and store it in a file.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(data, filename):
    """
    Convert a dictionary to XML format and save it to a file.

    Args:
        data (dict): The dictionary to convert.
        filename (str): The file to write the XML data to.
    """
    root = ET.Element('data')

    for key, value in data.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Load a dictionary from an XML file.

    Args:
        filename (str): The file to read the XML data from.

    Returns:
        dict: The dictionary loaded from the XML file.
    """
    root = ET.parse(filename).getroot()
    return {child.tag: child.text for child in root}
