#!/usr/bin/python3

"""
This module provides the function 'add_integer',
which adds two integers or floats
(after converting floats to integers).
It raises a TypeError if the inputs are not integers or floats.

Example:
    >>> add_integer(1, 2)
    3
"""


def add_integer(a, b=98):
    """
    Computes the sum of two integers. Floats are converted to integers.

    Args:
    a (int or float): first parameter
    b (int or float, optional): second parameter, default is 98

    Raises:
        TypeError: if a or b is not an integer or float.

    Returns:
    int: The sum of the two parameters, with floats converted to integers.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
