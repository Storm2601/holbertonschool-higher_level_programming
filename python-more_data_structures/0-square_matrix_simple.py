#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for i in range(len(matrix)):
        squared_row = []
        for j in range(len(matrix[i])):
            squared_row.append(matrix[i][j] ** 2)
        square_matrix.append(squared_row)
    return square_matrix
