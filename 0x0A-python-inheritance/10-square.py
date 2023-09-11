#!/usr/bin/python3
"""defines a class rectangle that inherits BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry defined"""

    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates if a number is int"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """defines class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initializes class Rectangle

        Args: width: rectangle width
        height: rectangle height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """class Square defined"""

    def __init__(self, size):
        """class square initialized"""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        return f"[Rectangle] {self._Rectangle__width}/{self._Rectangle__height}"
