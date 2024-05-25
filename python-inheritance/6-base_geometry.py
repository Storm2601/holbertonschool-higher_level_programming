#!/usr/bin/python3
"""class with a method that raise and exception"""


class BaseGeometry():
    """class with a method to raise area"""
    def area(self):
        """raises an Exception with the message"""
        raise Exception("area() is not implemented")
