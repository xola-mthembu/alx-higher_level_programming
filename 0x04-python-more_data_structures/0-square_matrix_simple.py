#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.
    Args:
    matrix (list of lists): A 2D array.
    Returns:
    list of lists: New matrix with squared values.
    """
    return [list(map(lambda x: x**2, row)) for row in matrix]
