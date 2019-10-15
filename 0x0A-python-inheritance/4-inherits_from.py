#!/usr/bin/python3
def inherits_from(obj, a_class):
    """function that returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class ; otherwise
    False.
    """
    if isinstance(obj, a_class) and not issubclass(a_class, type(obj)):
        return True
    else:
        return False
