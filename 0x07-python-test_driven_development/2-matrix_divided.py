#!/usr/bin/python3
def matrix_divided(matrix, div):
    errormessage = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(errormessage)
    if not isinstance(matrix, list):
        raise TypeError(errormessage)
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(errormessage)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        if len(row) == 0:
            raise TypeError(errormessage)

        for item in row:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError(errormessage)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
