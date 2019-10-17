#!/usr/bin/python3
"""Module ´´4-append_write´´ with append_write function"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a text file (UTF8)
    Args:
        filename (str): string of the filename
        text (str): text to append
    Returns:
        Number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        count = f.write(text)
    return count
