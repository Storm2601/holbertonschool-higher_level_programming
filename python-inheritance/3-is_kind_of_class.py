#!/usr/bin/python3
"""function that returns True if the object is an instance
   or if the object is an instance of a class that inherited
   from, the specified class ; otherwise False"""

def is_kind_of_class(obj, a_class):
    """return true or false if object is an instance"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
