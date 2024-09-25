#!/usr/bin/python3
"""Rectangle class that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """Representation of a rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
