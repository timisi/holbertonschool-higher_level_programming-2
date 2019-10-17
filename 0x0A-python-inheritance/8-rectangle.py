#!/usr/bin/python3
"""Module ´´8-rectangle´´ with BaseGeometry class and Rectanble class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
