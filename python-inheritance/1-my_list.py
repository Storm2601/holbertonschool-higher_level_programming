#!/usr/bin/python3
"""Mylist that inherits from list"""


class MyList(list):
    """that prints the list, but sorted (ascending sort)"""
    def print_sorted(self):
        print(sorted(self))