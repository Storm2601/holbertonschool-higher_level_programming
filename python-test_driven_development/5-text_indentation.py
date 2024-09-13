#!/usr/bin/python3
"""This module defines the text_indentation function."""


def text_indentation(text):
    """Prints a string with 2 blank lines after '.', '?', and ':' characters.

    Args:
        text (str): The input string to format.

    Raises:
        TypeError: If the input is not a string.
    """
    if isinstance(text, str):
        s1 = text.replace(". ", ".\n")
        s1 = s1.replace("? ", "?\n")
        s1 = s1.replace(": ", ":\n")

        for i in range(len(s1)):
            if s1[i] in ".?:":
                print(s1[i], end="")
                print()
            else:
                print(s1[i], end="")
    else:
        raise TypeError("text must be a string")
