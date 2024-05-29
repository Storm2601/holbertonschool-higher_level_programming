#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """retrieves a dictionary representation of a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dictionary description with simple data structure"""
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    result[key] = value
            return result

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
