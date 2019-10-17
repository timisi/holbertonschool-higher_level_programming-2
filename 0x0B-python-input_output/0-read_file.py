#!/usr/bin/python3
"""Module ´´0-read_file´´ with read_file function"""


def read_file(filename=""):
    """Function that reads a text file (UTF8) and prints it to stdout
    Args:
        filename (str): string of the filename
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
