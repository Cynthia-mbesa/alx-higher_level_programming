#!/usr/bin/python3
"""defines a Square class"""


class Square:
    """Square class with private instance attribute 'size'"""

    def __init__(self, size):
        """initialize a new Square instance.

        Args:
        size (int): The size of the Square.
        """
        self.__size = size
