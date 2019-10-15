#!/usr/bin/python3
class MyInt(int):
    """class MyInt that inherits from int and modify methods
    Args:
        int (class): patern class
    """
    def __init__(self, value):
        """Instantiation of the integer"""
        self.integer = value

    def __eq__(self, other_int):
        return self.integer != other_int

    def __ne__(self, other_int):
        return self.integer == other_int
