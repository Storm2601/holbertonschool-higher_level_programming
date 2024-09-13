#!/usr/bin/python3

"""
This module divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number and rounds the result
    to 2 decimal places.

    Parameters:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int/float): The number by which each element of the matrix
                          will be divided.

    Returns:
        list of lists of float: A new matrix with each element divided by div.

    Raises:
        TypeError: If matrix is not a matrix (list of lists)
        of integers/floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """

    # Validate that matrix is a list of lists
    if (not isinstance(matrix, list) or not matrix or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # Validate that all rows of the matrix have the same length
    first_row_length = len(matrix[0])
    if not all(len(row) == first_row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate that div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Validate that div is not zero to avoid division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create a new matrix with each element divided by div and rounded
    # to 2 decimal places
    new_matrix = []
    for row in matrix:
        new_matrix.append([round(element / div, 2) for element in row])

    return new_matrix
