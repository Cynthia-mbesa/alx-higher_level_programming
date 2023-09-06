#!/usr/bin/python3
"""1-rectangle - defines a Rectangle class"""


class Rectangle:
    """class representing a rectangle"""
    def __init__(self, width=0, height=0):
        """initializes a new Rectangle instance

        Args: width(int): width of rectangle
        height(int): height of rectangle

        Raises:
        TypeError: width or height not integer
        ValueError: wwidth or height < 0
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """get width of rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            """set width

            Args: value(int):width value
            """
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """get height"""
            return self.__height

        @height.setter
        def height(self, value):
            """set height value

            Args: value(int): height value
            """
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
