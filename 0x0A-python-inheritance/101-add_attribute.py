#!/usr/bin/python3
def add_attribute(obj, name="", value=""):
    if isinstance(setattr(obj, name, value), Exception):
        raise TypeError("can't add new attribute")
