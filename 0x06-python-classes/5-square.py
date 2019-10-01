#!/usr/bin/python3
class Square:
    """Defines a square by size."""
    def __init__(self, size=0):
        """Initializes the data.
        Args:
            size (int): value of the size
        """
        self.__size = size

    def area(self):
        """Returns current square area"""
        return (self.__size ** 2)

    @property
    def size(self):
        """getter __size private instance attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
            if value < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """Prints the square with # char"""
        if self.size == 0:
            print()
        else:
            for row in range(self.size):
                    print(("#" * self.size), end="")
                    print()
