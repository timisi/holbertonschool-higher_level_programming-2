#!/usr/bin/python3
""" Module: 4-print_square
Contain function print_square that print a square with # char

    Testing: use tests/4-print_square.txt with doctest()
"""


def print_square(size):
    """Prints the square with # char
    Arg:
        size (int): size of the square
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if isinstance(size, float):
        size = int(size)
    if isinstance(size, int):
        if size < 0:
            raise ValueError("size must be >= 0")
    else:
        raise TypeError("size must be an integer")
    if size == 0:
        print()
    else:
        for row in range(size):
            print("#" * size)
