#!/usr/bin/python3

"""Function that opens and prints the content of a .txt file."""


def read_file(filename=""):
    """
    Opens a text file with UTF-8 encoding and prints its content.

    Args:
        filename (str): The name of the file to open. If not provided, an
        empty string is used by default.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
