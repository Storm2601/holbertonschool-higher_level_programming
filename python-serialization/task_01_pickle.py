#!/usr/bin/python3

"""
Class management module with serialization and deserialization capabilities.
"""

import pickle


class CustomObject:
    """
    A class representing a custom object with 3 specifics attributes.

    Attributes:
        name (str): The name assigned to the object.
        age (int): The age of the object.
        is_student (bool): Indicates if the object represents a student.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize the object with the values supplied by the constructor.

        Args:
            name (str): The name of the object.
            age (int): The age of the object.
            is_student (bool): Defines if the object is a student or not.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Displays the object's attributes in a clear and readable format.
        """
        print(f"Name: {self.name}\n"
              f"Age: {self.age}\n"
              f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Saves the current object state to a specified file.

        Args:
            filename (str): The path of the file where
            the object will be stored.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Unable to save object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Restores an object from a specified file.

        Args:
            filename (str): The path to the file from which to load the object.

        Returns:
            CustomObject: The reconstructed object from the file,
            or None on failure.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (EOFError, pickle.PickleError, FileNotFoundError) as e:
            print(f"Failed to load object: {e}")
            return None
