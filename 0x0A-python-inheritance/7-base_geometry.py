#!/usr/bin/python3
"""Module ´´7-base_geometry´´ with BaseGeometry class"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """function that raise an error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates value
        Args:
            name (str): name of the int attribute
            value (int): value of the attribute
        """
        if not issubclass(int, type(value)) or not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
