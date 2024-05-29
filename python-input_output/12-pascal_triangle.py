#!/usr/bin/python3
"""function that returns a list of lists of integers
    representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """function that returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(0, n - 1):
        row = [1]
        for j in range(0, i):
            row.append(triangle[i][j] + triangle[i][j + 1])
        row.append(1)
        triangle.append(row)
    return triangle
