#!/usr/bin/python3
"""Module ´´5-to_json_string´´ with to_json_string function"""


import json


def to_json_string(my_obj):
    """Function that encode an object to JSON
    Args:
        my_obj (object): object to be encoded
    Returns:
        The JSON representation of an object (string)
    """
    return json.dumps(my_obj)
