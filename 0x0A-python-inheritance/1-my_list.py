#!/usr/bin/python3
class MyList(list):
    """Class MyList that inherits from list
    """

    def __init__(self):
        """__init__ method inherit from list"""
        super().__init__()

    def print_sorted(self):
        """method that prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
