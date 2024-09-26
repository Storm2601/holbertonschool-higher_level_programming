#!/usr/bin/python3

"""Iterator class that counts the number of elements it iterates over."""


class CountedIterator:
    """An iterator that keeps track of how many items have been iterated."""

    def __init__(self, iterable):
        """Initializes the iterator and a counter to track iterations.

        Args:
            iterable: Any iterable object like a list, tuple, etc.
        """
        self._iterator = iter(iterable)
        self._count = 0

    def get_count(self):
        """Returns the current count of items iterated.

        Returns:
            int: The number of items iterated over.
        """
        return self._count

    def __next__(self):
        """Returns the next item from the iterable and increments the count.

        Returns:
            The next item from the iterable.

        Raises:
            StopIteration: If there are no more items in the iterable.
        """
        try:
            item = next(self._iterator)
            self._count += 1
            return item
        except StopIteration:
            raise StopIteration
