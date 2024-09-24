#!/usr/bin/python3
"""
This module defines the BaseGeometry class with an area method
that raises an exception.
"""


class BaseGeometry:
    """A class representing basic geometric properties."""

    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            Exception: area() is not implemented.
        """
        raise Exception("area() is not implemented")
