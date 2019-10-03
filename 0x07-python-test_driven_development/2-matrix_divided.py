#!/usr/bin/python3
""" Module: 2-matrix_divided
Contain the matrix_divided function that return the division of all elements
of a matrix.

    Testing: use tests/tests/2-matrix_divided.txt with doctest()
"""


def matrix_divided(matrix, div):
    """matrix_divided function that divides all elements of a matrix.
    Args:
        matrix (list): list of lists of integers/floats
        div (int, float): Non-Zero number
    Returns:
        matrix of results
    """
    er_msj_1 = "matrix must be a matrix (list of lists) of integers/floats"
    er_msj_2 = "Each row of the matrix must have the same size"
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(er_msj_1)
    len_list_num_0 = len(matrix[0])

    # Div verif
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Matrix verif
    for idx in range(len(matrix)):
        if not isinstance(matrix[idx], list) or not matrix[idx]:
            raise TypeError(er_msj_1)
        if len_list_num_0 != len(matrix[idx]):
            raise TypeError(er_msj_2)
        for n in matrix[idx]:
            if not isinstance(n, int) and not isinstance(n, float):
                raise TypeError(er_msj_1)

    new_matrix = []
    for i in range(len(matrix)):
        new_matrix += [list(map(lambda x: round((x / div), 2), matrix[i]))]
    return new_matrix
