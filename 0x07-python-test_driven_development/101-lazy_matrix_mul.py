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
    # list m_a and m_b
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # list of lists m_a and m_b
    for idx in range(len(m_a)):
        if not isinstance(m_a[idx], list):
            raise TypeError("m_a must be a list of lists")
    for idx in range(len(m_b)):
        if not isinstance(m_b[idx], list):
            raise TypeError("m_b must be a list of lists")

    # m_a and m_b not empty
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for idx in range(len(m_a)):
        if len(m_a[idx]) == 0:
            raise ValueError("m_a can't be empty")
    for idx in range(len(m_b)):
        if len(m_b[idx]) == 0:
            raise ValueError("m_b can't be empty")

    # type must be integer of float
    for idx in range(len(m_a)):
        for n in m_a[idx]:
            if not isinstance(n, int) and not isinstance(n, float):
                raise ValueError("m_a should contain only integers or floats")
    for idx in range(len(m_b)):
        for n in m_b[idx]:
            if not isinstance(n, int) and not isinstance(n, float):
                raise ValueError("m_b should contain only integers or floats")

    # each row must be of the same size
    len_list_a_0 = len(m_a[0])
    for idx in range(len(m_a)):
        if len(m_a[idx]) != len_list_a_0:
            raise TypeError("each row of m_a must be of the same size")
    len_list_b_0 = len(m_b[0])
    for idx in range(len(m_b)):
        if len(m_b[idx]) != len_list_b_0:
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    out = []
    m_a = np.array(m_a)
    m_b = np.array(m_b)

    out = m_a.dot(m_b)
    return out
