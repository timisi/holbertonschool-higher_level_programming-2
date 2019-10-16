#!/usr/bin/python3
"""Module ´´2-is_same_class´´ with is_same_class function"""


def is_same_class(obj, a_class):
    """Function that returns True if the object is exactly an instance of the
    specified class ; otherwise False.
    Args:
        obj (object): given object
        a_class (class): class to be compared
    Returns:
        if the object is exactly an instance of the specified class
    """
    if isinstance(obj, a_class) and issubclass(a_class, type(obj)):
        return True
    else:
        return False
