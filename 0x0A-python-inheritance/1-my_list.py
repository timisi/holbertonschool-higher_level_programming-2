#!/usr/bin/python3
class MyList(list):
    """Class MyList that inherits from list
    """

    def print_sorted(self):
        """method that prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
