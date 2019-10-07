#!/usr/bin/python3
class Rectangle:
    """Empty class Rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes the data.
        Args:
            width (int): value of the widht
            height (int): value of the widht
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        type(self).number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter __width private instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter __height private instance attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the current rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Returns the current rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.height * 2) + (self.width * 2))

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        str_rep = ""
        for h in range(self.__height):
            str_rep = str_rep + ("#" * self.__width) + "\n"
        return str_rep[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, str(self.__height))

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
