#!/usr/bin/python3

"""
This module defines a function to print a first name and a last name.

The function expects both the first name and last name to be strings.
If the arguments are not of type `str`, it raises a `TypeError`.

Functions:
    say_my_name(first_name, last_name=""): Prints the full name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a formatted string with the first name and last name.

    Args:
        first_name (str): The first name to print.
        last_name (str, optional): The last name to print.
        Defaults to an empty string.

    Raises:
        TypeError: If `first_name` or `last_name` is not a string.

    Example:
        say_my_name("John", "Smith")
        Output: My name is John Smith
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
