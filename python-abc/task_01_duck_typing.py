#!/usr/bin/env python3

"""
Defines an abstract class for shapes and concrete implementations 
for specific shapes (Circle, Rectangle).
"""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.
    Requires the implementation of area and perimeter methods.
    """

    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.
        Must be implemented by subclasses.
        """
        pass


class Circle(Shape):
    """
    A concrete class representing a circle.

    Attributes:
    radius (float): The radius of the circle.
    """

    def __init__(self, radius):
        """
        Initializes a Circle instance with the given radius.

        Args:
        radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
        float: The area of the circle.
        """
        return abs(math.pi * self.radius**2)

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.

        Returns:
        float: The perimeter of the circle.
        """
        return abs(2 * math.pi * self.radius)


class Rectangle(Shape):
    """
    A concrete class representing a rectangle.

    Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with the given width and height.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
        int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
        int: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a given shape object.

    Args:
    shape (Shape): An object that inherits from the Shape class.

    Returns:
    None
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
