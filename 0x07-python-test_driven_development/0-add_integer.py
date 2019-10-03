#!/usr/bin/python3
""" Module: 0-add_integer
    Contain the add_integer function that return the add of two integers
    Testing: use tests/0-add_integer.txt with doctest()

"""


def add_integer(a, b=98):
    """add_integer function that add 2 integers
    Args:
        a (int, float): fistr number
        b (int, float): second number
    Returns:
        the addition of a and b
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int):
        raise TypeError("b must be an integer")
    else:
        return a + b
