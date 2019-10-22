#!/usr/bin/python3
"""module with Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits Rectangle class
    Args:
        Rectangle (class): Rectangle class
    Attribures:
        size (int): size
        x (int): x axis
        y (int): y axis
        id: instance id
    """
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor
        Args:
            size (int): size
            x (int): x axis
            y (int): y axis
            id (int): instance public attribute
        """
        super().__init__(size, size, x, y, id)
        self.__size = self.width = self.height

    @property
    def size(self):
        """getter __size private instance attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__size = value
        else:
            raise TypeError("width must be an integer")

    def __str__(self):
        print_data = (self.id, self.x, self.y, self.size)
        return ("[Square] ({}) {}/{} - {}".format(*print_data))

    def update(self, *args, **kwargs):
        """Public method that assigns an argument to each attribute"""
        attr_name = ['id', 'size', 'x', 'y']
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
        obj_dict['size'] = self.size
        obj_dict['x'] = self.x
        obj_dict['y'] = self.y
        return obj_dict
