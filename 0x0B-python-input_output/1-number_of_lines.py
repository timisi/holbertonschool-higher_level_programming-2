#!/usr/bin/python3
"""Module ´´1-number_of_lines´´ with number_of_lines function"""


def number_of_lines(filename=""):
    """Function that count the number of lines of a text file
    Args:
        filename (str): string of the filename
    Returns:
         Number of lines of a text file
    """
    count = 0
    with open(filename, encoding="utf-8") as f:
        for line in f:
            count += 1
    return count
