#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr_fun = lambda x : x ** 2
    new_matrix =[]
    for i in range(len(matrix)):
        new_matrix += [list(map(sqr_fun, matrix[i]))]

    return new_matrix
