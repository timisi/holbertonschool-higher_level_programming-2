#!/usr/bin/python3
"""Module ´´3-write_file´´ with write_file function"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file (UTF8)
    Args:
        filename (str): string of the filename
        text (str): text to write
    Returns:
        Number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        count = f.write(text)
    return count
