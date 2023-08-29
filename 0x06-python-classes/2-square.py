#!/usr/bin/python3
"""defines a Square class"""


class Square:
    """Square class with a private attribute 'size'"""

    def __init__(self, size=0):
        """initializes a new Square instance

        Argas:
        size (int, optional): size of Square, default to 0.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
