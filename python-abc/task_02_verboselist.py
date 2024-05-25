#!/usr/bin/python3
class VerboseList(list):
    """This custom class should print a notification message"""

    def append(self, item):
        """Add an item"""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        """Extend the list"""
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        """Remove the first occurrence of the item"""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        item = super().pop(index)
        """Remove and return the item at the given index"""
        print("Popped [{}] from the list.".format(item))
        return item
