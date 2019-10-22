#!/usr/bin/python3
"""module with Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits Base class
    Args:
        Base (class): Base class
    Attribures:
        width (int): width
        height (int): height
        x (int): x axis
        y (int): y axis
        id: instance id
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor
        Args:
            width (int): width
            height (int): height
            x (int): x axis
            y (int): y axis
            id (int): instance public attribute
        """
        super().__init__(id)
        if type(width) is int:
            if width <= 0:
                raise ValueError("width must be > 0")
            self.__width = width
        else:
            raise TypeError("width must be an integer")
        if type(height) is int:
            if height <= 0:
                raise ValueError("height must be > 0")
            self.__height = height
        else:
            raise TypeError("height must be an integer")
        if type(x) is int:
            if x < 0:
                raise ValueError("x must be >= 0")
            self.__x = x
        else:
            raise TypeError("x must be an integer")
        if type(y) is int:
            if y < 0:
                raise ValueError("y must be >= 0")
            self.__y = y
        else:
            raise TypeError("y must be an integer")

    @property
    def width(self):
        """getter __width private instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is int:
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """getter __height private instance attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is int:
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """getter __x private instance attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """getter __y private instance attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """Public method that return Area"""
        return self.__width * self.__height

    def display(self):
        """Public method that prints in stdout the Rectangle instance with the
        character #"""
        for i in range(self.y):
            print()
        for row in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        print_data = (self.id, self.x, self.y, self.width, self.height)
        return "[Rectangle] ({}) {}/{} - {}/{}".format(*print_data)

    def update(self, *args, **kwargs):
        """Public method that assigns an argument to each attribute"""
        attr_name = ['id', 'width', 'height', 'x', 'y']
        if args and args != ():
            i = 0
            for argum in args:
                try:
                    setattr(self, attr_name[i], argum)
                    i += 1
                except IndexError:
                    pass
        else:
            for k, v in kwargs.items():
                if k in attr_name:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Public method hat returns the dictionary representation of a
        Rectangle
        """
        obj_dict = {}
        obj_dict['id'] = self.id
        obj_dict['width'] = self.width
        obj_dict['height'] = self.height
        obj_dict['x'] = self.x
        obj_dict['y'] = self.y
        return obj_dict
