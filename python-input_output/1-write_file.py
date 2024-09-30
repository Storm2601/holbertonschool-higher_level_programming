#!/usr/bin/python3

"""Function that writes a string to a text file (UTF-8)
and returns the number of characters written."""


def write_file(filename="", text=""):
    """
    Writes the given string to a specified file using UTF-8 encoding.

    Args:
        filename (str): The name of the file to write to. If the file does
        not exist, it will be created. If it exists, its content will
        be overwritten.
        text (str): The string to write into the file.

    Returns:
        int: The number of characters successfully written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        written = file.write(text)
        return written
