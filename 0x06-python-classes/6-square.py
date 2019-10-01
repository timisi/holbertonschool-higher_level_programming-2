#!/usr/bin/python3
"""Write a class Square that define a square by size"""
class Square:
    """Defines a square by size."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data.
        Args:
            size (int): value of the size
            position (tuple): position to print, two positive integers
        """
        if isinstance(size, int):
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        if isinstance(position, tuple) and len(position) == 2 and position[0] >= 0 and position[1] >= 0:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        """getter __size private instance attribute"""
        return self.__position
    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2 and position[0] >= 0 and position[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """Prints the square with # char"""
        if self.size == 0:
            print()
        else:
            if self.position[1] > 0:
                print("\n" * self.position[1], end="")
            for row in range(self.size):
                if self.position[0] > 0:
                    print(" " * self.position[0], end="")
                print("#" * self.size)
