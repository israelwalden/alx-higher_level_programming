#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [list(map(lambda x: x ** 2, _)) for _ in matrix]
    return new_matrix
