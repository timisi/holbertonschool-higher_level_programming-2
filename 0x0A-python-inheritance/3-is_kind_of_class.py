#!/usr/bin/python3
"""Module ´´3-is_kind_of_class´´ with is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Function that verify the kind of class
    Args:
        obj (object): given object
        a_class (class): class to be compared
    Returns:
        True if the object is an instance of, or if the object is an instance
        of a class that inherited from, the specified class, otherwise False.
    """
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    else:
        return False
