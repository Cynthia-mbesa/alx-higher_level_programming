#!/usr/bin/python3
"""module containing student class"""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        """instantiates a student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary representation of student"""
        return self.__dict__
