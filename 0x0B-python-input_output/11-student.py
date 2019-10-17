#!/usr/bin/python3
"""Module ´´11-student´´ with class Student"""


class Student:
    """Class Student
    Attributes:
        first_name (str): name
        last_name (str): last name
        age (int): age of student
    """
    def __init__(self, first_name, last_name, age):
        """Instantiation of attributes
        Args:
            first_name (str): name
            last_name (str): last name
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Function that returns the dictionary description with simple data
        structure (list, dictionary, string, integer and boolean) for JSON
        serialization of an object
        """
        return self.__dict__
