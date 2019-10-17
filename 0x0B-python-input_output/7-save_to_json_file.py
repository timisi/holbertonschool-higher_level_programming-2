#!/usr/bin/python3
"""Module ´´7-save_to_json_file´´ with save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file, using a JSON
    representation
    Args:
        my_obj (object): python object
        filename (str): file use
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
