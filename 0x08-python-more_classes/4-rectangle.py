#!/usr/bin/python3
""""4-rectangle - defines a rectangle class"""


class Rectangle:
    """defines a rectangle by width and height"""

    def __init__(self, width=0, height=0):
        """initializes anew rectangle

        Args: width (int, optional): rectangle width, default 0
        height(int, optional): rectangle height, default 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method for width"""
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
        """setter method for height
        Args: value(int): height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate rectangle area"""
        return self.__width * self.__height

    def perimeter(sellf):
        """calculate rectangle perimeter"""
        if self.__width == 0 or self.__height == o:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """return a string rep of rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(['#' * self.__width] * self.__height)

    def __repr__(self):
        """return string rep of rectangle"""
        return f"Rectangle({self.width}, {self.height})"
