#!/usr/bin/python3
"""5-rectangle - defines a rectangle class"""


class Rectangle:
    """class representing a rectangle"""
    def __init__(self, width=0, height=0):
        """initializes a new rectangle

        Args:width(int): rectangle width
        height(int):rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method for rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width

        Args: value(int): width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """"setter method for height

        Args: value(int): height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate rectangle are"""
        return self.__width * self.__height

    def perimeter(self):
        """calculate rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """return string rep of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(['#' * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """return a string rep of rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """prints message when an instance of rectangle is deleted"""
        print("Bye rectangle...")
