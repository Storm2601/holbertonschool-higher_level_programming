#!/usr/bin/python3
"""create a function that returns a rectangle"""


class Rectangle:
    """class rectangle with private widht and private lenght
return: area
return: perimeter
print via __str__ a string representation of a rectangle
print message when delted with __del__
return: via __repr__ a representation of the rectangle used by eval
"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initiate new instance for each call of method in main"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    def __del__(self):
        """print a message when deleting an instance of rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1

    @property
    def width(self):
        """retrieve the private value of with"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """get the value value of width if is int and positiv number"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrieve the private value of height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """get the value value of width if is int and positiv number"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """return the area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """return the permimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """returns string representation of rectangle"""

        if self.__width == 0 or self.__height == 0:
            return ""

        rows = ["#" * self.__width for i in range(self.__height)]
        return "\n".join(rows)

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
