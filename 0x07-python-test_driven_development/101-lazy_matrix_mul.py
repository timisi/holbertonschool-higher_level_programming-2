#!/usr/bin/python3
""" Module that that multiplies 2 matrices
Contain the matrix_mul function that return the mul of all elements
of a matrix.

    Testing: use tests/100-matrix_mul.txt with doctest()
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """lazy_matrix_mul function that multiply all elements of a matrix.
    Args:
        m_a (list): list of lists of integers/floats
        m_b (list): list of lists of integers/floats
    Returns:
        matrix of results
    """
    return np.matmul(m_a, m_b)
