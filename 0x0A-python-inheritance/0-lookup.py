#!/usr/bin/python3
"""Module ´´0-lookup´´ with lookup function"""


def lookup(obj):
    """function that returns the list of available attributes and methods of
    an object
    Args:
        obj (object): object to be dir
    Returns:
        directory of the object
    """
    return dir(obj)
