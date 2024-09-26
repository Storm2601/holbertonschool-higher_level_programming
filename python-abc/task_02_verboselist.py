#!/usr/bin/python3
""" This module defines a custom list class `VerboseList` which extends the
functionality of Python's built-in list by printing a notification message
whenever the list is modified (e.g., adding, removing, or extending items).
"""
class VerboseList(list):
    """Custom list class that prints a message on each modification."""


    def append(self, item):
        """
        Add an item to the list and print a confirmation message.

        Args:
            item: The element to append to the list.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))


    def extend(self, item):
        """
        Extend the list by appending elements from another iterable.

        Args:
            item: The iterable whose elements are added to the list.
        """
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))


    def remove(self, item):
        """
        Remove the first occurrence of the specified item and print a message.

        Args:
            item: The element to remove from the list.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)


    def pop(self, index=-1):
        """
        Remove and return the item at the specified index, and print a message.

        Args:
            index: The position of the item to remove, defaults to -1 (last).

        Returns:
            The removed item.
        """
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
