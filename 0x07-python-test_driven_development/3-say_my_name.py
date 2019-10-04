#!/usr/bin/python3
""" Module: 3-say_my_name
Contain function say_my_name that print the first and last name given

    Testing: use tests/3-say_my_name.txt with doctest()
"""


def say_my_name(first_name, last_name=""):
    """say_my_name function that print first and last name given
    Args:
        first_name (str): first name argument
        last_name (str): last name argument
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
