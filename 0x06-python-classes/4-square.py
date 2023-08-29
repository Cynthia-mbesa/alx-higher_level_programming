#!/usr/bin/python3
"""define a Square class"""


class Square:
    """Square class with a private attribute 'size'
    and a public method 'area'
    """

    def __init__(self, size=0):
        """initializes a new Square instance

        Args:
        size(int, optional): size of Square, default to 0
        """
        self.__size = size

    @property
    def size(self):
        """getter method to retrieve the value of 'size'"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter method to set the value of 'size'

        Args:
        value (int): size value to be set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size mustbe >= 0")
        self.__size = value

    def area(self):
        """calculate and return the area of Square"""
        return self.__size ** 2
