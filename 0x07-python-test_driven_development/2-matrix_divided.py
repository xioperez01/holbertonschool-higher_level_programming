#!/usr/bin/python3
"""
Function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Returns a matrix
    """
    new = []
    error = "matrix must be a matrix (list of lists) of integers/floats"

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) != list:
        raise TypeError(error)

    for i in range(len(matrix)):
        if type(matrix[i]) != list:
            raise TypeError(error)
        elif len(matrix[0]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        else:
            index = []
            for j in range(len(matrix[i])):
                if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                    raise TypeError(error)
                else:
                    index.append(round((matrix[i][j] / div), 2))
            new.append(index)
    return new
