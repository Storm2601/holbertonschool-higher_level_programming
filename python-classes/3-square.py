#!/usr/bin/python3

"""Creates a class Square."""


class Square:
    """Defines a square."""
    def __init__(self, size=0):
        """Initializing size.
        Args :
            size: size of square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size
