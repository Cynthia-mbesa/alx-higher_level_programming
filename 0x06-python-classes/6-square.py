#!/usr/bin/python3
"""define a Square class"""


class Square:
    """Square class with a private attribute 'size' and 'position',
    and a public method 'area' and 'my_print'
    """

    def __init__(self, size=0, position=(0, 0)):
        """initializes a new Square instance

        Args:
        size(int, optional): size of Square, default to 0
        position (tuple, optional): position of Square, default to 0, 0
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """getting method to retrieve value of 'position'"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter method to set value of 'position'

        Args:
        value (tuple): position value to be set
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculate and return the area of Square"""
        return self.__size ** 2

    def my_print(self):
        """prints the Square using '#' characters"""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
