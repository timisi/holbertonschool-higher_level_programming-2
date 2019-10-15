#!/usr/bin/python3
class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """function that raise an error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates value"""
        if not issubclass(int, type(value)) or not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """class Rectangle inherit from BaseGeometry
    Args:
        BaseGeometry (class): patern class
    """
    def __init__(self, width, height):
        """Instantiation of width and height with validation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
