#!/usr/bin/python3
"""Module ´´11-square´´ with BaseGeometry class, Rectanble class
and Square class"""


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

    def area(self):
        """function that returns the area"""
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """class Square inherit from Rectangle
    Args:
        Rectangle (class): patern class
    Attributes:
        __size (int): positive integer
    """
    def __init__(self, size):
        """Instantiation of size with validation
        Args:
            size (int): positive integer
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """function that returns the area"""
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
