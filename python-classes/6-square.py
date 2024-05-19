#!/usr/bin/python3

"""Creates a class Square"""


class Square:
    """Defines a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializing size.
        Args :
            size: size of square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves the position."""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with #."""
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__position[1]):
                print("")
            for i in range(0, self.__size):
                for j in range(0, self.__position[0]):
                    print(" ", end="")
                for k in range(0, self.__size):
                    print("#", end="")
                print("")
