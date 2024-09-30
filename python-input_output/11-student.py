#!/usr/bin/python3
"""Class Student that defines a student."""


class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representing the Student instance.

        Args:
            attrs (list): Optional list of attribute names to include
            in the dictionary.

        Returns:
            dict: A dictionary containing the instance's attributes.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {
                attr: self.__dict__[attr]
                for attr in attrs if attr in self.__dict__
            }

    def reload_from_json(self, json):
        """
        Replaces all instance attributes with values from the
        provided JSON dictionary.

        Args:
            json (dict): A dictionary containing new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
