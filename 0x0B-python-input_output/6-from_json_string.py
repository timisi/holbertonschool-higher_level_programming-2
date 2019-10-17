#!/usr/bin/python3
"""Module ´´6-from_json_string´´ with to_json_string function"""


import json


def from_json_string(my_str):
    """Function take a JSON string an decode to python data structure
    Args:
        my_str (str): JSON string
    Returns:
        An object (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
