#!/usr/bin/python3
"""Module ´´8-load_from_json_file´´ with load_from_json_file function"""


import json


def load_from_json_file(filename):
    """Function that creates an Object from a “JSON file”
    Args:
        filename (str): sourse json file to use
    """
    with open(filename, "r", encoding="utf-8") as f:
        obj_str = f.read()
    return json.loads(obj_str)
