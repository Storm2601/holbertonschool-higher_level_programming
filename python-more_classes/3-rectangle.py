#!/usr/bin/python3

"""Creates an class Rectangle"""


class Rectangle:
    """Defines a rectangle."""
    def __init__(self, width=0, height=0):
        """Initializing size.
        Args :
            width: width of rectangle.
            height: height of rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns current width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns current height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the current rectangle area."""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the current rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Prints the rectangle with #."""
        rectangle = ""

        if self.__width == 0 or self.__height == 0:
            return rectangle

        for height in range(self.__height):
            for width in range(self.__width):
                rectangle += "#"
            rectangle += "\n"
        rectangle = rectangle[:-1]
        return rectangle
