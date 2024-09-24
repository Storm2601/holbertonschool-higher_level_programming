#!/usr/bin/python3
"""This module defines a BaseGeometry class for geometric operations."""


class BaseGeometry:
    """A class representing basic geometric operations."""

    def area(self):
        """Calculates the area of the geometry.

        Raises:
            Exception: area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if the value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
