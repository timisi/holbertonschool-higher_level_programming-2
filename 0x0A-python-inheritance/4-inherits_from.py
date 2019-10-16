#!/usr/bin/python3
"""Module ´´4-inherits_from´´ with inherits_from function"""


def inherits_from(obj, a_class):
    """Function that verify the inherits property
    Args:
        obj (object): given object
        a_class (class): class to be compared
    Returns:
        True if the object is an instance of a class that inherited (directly
        or indirectly) from the specified class ; otherwise False.
    """
    if isinstance(obj, a_class) and not issubclass(a_class, type(obj)):
        return True
    else:
        return False
