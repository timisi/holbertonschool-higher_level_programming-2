#!/usr/bin/python3
"""Module ´´8-rectangle´´ with BaseGeometry class and Rectanble class"""


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


class Rectangle(BaseGeometry):
    """class Rectangle inherit from BaseGeometry
    Args:
        BaseGeometry (class): patern class
    Attributes:
        __width (int): positive integer
        __height (int): positive integer
    """
    def __init__(self, width, height):
        """Instantiation of width and height with validation
        Args:
            width (int): positive integer
            height (int): positive integer
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
