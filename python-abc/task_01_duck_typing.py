#!/usr/bin/env python3
"""class shape with abstract method area and perimeter"""


import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """abstract class from ABC"""
    @abstractmethod
    def area(self):
        """abstract method area"""
        pass

    @abstractmethod
    def perimeter(self):
        """abstract method perimeter"""
        pass


class Circle(Shape):
    """A class representing a circle, derived from the Shape class."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return abs(math.pi * (self.radius ** 2))

    def perimeter(self):
        """Calculate the perimeter of the circle."""
        return abs(2 * math.pi * self.radius)


class Rectangle(Shape):
    """class rectangle from shape with two methods are and perimeter"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """return area using width and height from init"""
        return (self.width * self.height)

    def perimeter(self):
        """return perimeter adding width and height by two"""
        return (2 * (self.width + self.height))


def shape_info(Shape):
    """shape method for duck typing"""
    print(f"Area: {Shape.area()}")
    print(f"Perimeter: {Shape.perimeter()}")
