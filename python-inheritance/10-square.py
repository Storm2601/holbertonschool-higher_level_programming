#!/usr/bin/python3
"""Square class that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """Representation of a square that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square.
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
