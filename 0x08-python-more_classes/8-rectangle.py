#!/usr/bin/python3
"""8-rectangle - defines a rectangle class"""


class Rectangle:
    """class repreenting a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes a new rectangle

        Args: width(int): rectangle width
        height(int): rectangle height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            raise ValueError("width must be >=0")
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
        """calculates rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns string rep of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(
                [str(self.print_symbol) * self.__width] * self.__height)

    def __repr__(self):
        """returns string rep of rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """prints message if instance of rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns biiger rectangle based on area

        Args: rect_1(Rectangle): first rectangle
        rect_2(Rectangle): second rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Recatngle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area1 = rect_1.area()
        area2 = rect_2.area()

        if area1 >= area2:
            return rect_1
        else:
            return rect_2
