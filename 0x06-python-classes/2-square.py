#!/usr/bin/python3
class Square:
    """Defines a square by size."""
    def __init__(self, size=0):
        """Initializes the data.
        Args:
            size (int): value of the size
        """
        if isinstance(size, int):
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
