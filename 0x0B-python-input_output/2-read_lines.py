#!/usr/bin/python3
"""Module ´´1-number_of_lines´´ with read_lines function"""


def read_lines(filename="", nb_lines=0):
    """Function that reads n lines of a text file (UTF8) and prints it to stdout
    Args:
        filename (str): string of the filename
        nb_lines (int): number of lines to print
    """
    count = 0
    with open(filename, encoding="utf-8") as f:
        for line in f:
            count += 1

    if nb_lines == 0 or nb_lines >= count:
        with open(filename, encoding="utf-8") as f:
            print(f.read(), end="")

    with open(filename, encoding="utf-8") as f:
        for n in range(nb_lines):
            print(f.readline(), end="")
