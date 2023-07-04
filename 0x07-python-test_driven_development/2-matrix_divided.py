#!/usr/bin/python3
"""
function within divides all elemets of a matrix
"""


def matrix_divided(matrix, div):
    """ divide all elements of a matrix"""

    is_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(is_matrix)
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(is_matrix)
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError(is_matrix)

    size_rows = [len(i) for i in matrix]  # each row of matrix must be same
    for k in size_rows:
        if k != size_rows[0]:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):  # div must be a number
        raise TypeError("div must be a number")

    if div == 0:  # handle division by zero case
        raise ZeroDivisionError("division by zero")

    return [[round(j/div, 2) for j in list_] for list_ in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
