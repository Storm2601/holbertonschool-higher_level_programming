#!/usr/bin/python3

"""
This module defines a function to print a square using the character '#'.

The size of the square is provided as an argument
and must be a positive integer.

Functions:
    print_square(size): Prints a square with the given size.
"""


def print_square(size):
    """
    Prints a square with the character '#',
    where each side has a length of `size`.

    Args:
        size (int): The length of each side of the square.
        Must be a non-negative integer.

    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is less than 0.

    Example:
        print_square(3)
        Output:
        ###
        ###
        ###
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
