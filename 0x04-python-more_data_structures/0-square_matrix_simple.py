#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list(map(lambda raw: list(map(lambda x: x*x, raw)), matrix))
    return new_matrix
