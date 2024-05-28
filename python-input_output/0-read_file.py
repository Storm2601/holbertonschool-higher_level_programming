#!/usr/bin/python3
"""function that print a file.txt"""


def read_file(filename=""):
    """open and print a file .txt"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
