#!/usr/bin/python3

""" fonction that devid matrix by an element """


def matrix_divided(matrix, div):
    """
    fonction take matrix and div

    args:
    matrix (int or float): first arg
    div (int or float diff from zero): second arg
    """
    if not (isinstance(matrix, list) and matrix) or not all(
        isinstance(row, list) and all(
            isinstance(element, (int, float))
            for element in row) for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_element = round(element/div, 2)
            new_row.append(new_element)
        new_matrix.append(new_row)
    return new_matrix
