#!/usr/bin/python3
"""The module defines a MyList class which inherits from list.
"""


class MyList(list):
    """A subclass of list that provides a method
    to print the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.

        The list elements are assumed to be of type int.
        """
        print(sorted(self))
