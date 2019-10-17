#!/usr/bin/python3
"""Module ´´100-append_after´´ with append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """Function that  inserts a line of text to a file, after each line
    containing a specific string
    Args:
        filename (str): string of the filename
        search_string (str): text to look
        new_string (str): text to append after.
    """
    final_txt = ""
    with open(filename) as f:
        for line in f:
            final_txt += line
            if search_string in line:
                final_txt += new_string

    with open(filename, "w") as f:
        f.write(final_txt)
