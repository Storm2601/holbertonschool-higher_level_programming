#!/usr/bin/python3

"""Creates a class Square."""


class Square:
    """Defines a square."""
    def __init__(self, size=0):
        """Initializing size.
        Args :
            size: size of square.
        """
        self.__size = size

    @property
    def size(self):
        """Returns curent size."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with #."""
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
