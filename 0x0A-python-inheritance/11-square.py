#!/usr/bin/python3
"""Module ´´11-square´´ with BaseGeometry class, Rectanble class
and Square class"""


Rectangle = __import__('9-rectangle').Rectangle


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
