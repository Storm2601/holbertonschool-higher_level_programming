#!/usr/bin/python3
"""CustomObject class with serialization and deserialization"""

import pickle


class CustomObject:
    """CustomObject class with name, age and is_student attributes"""

    def __init__(self, name, age, is_student):
        """Initialize the object attributes"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object attributes"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the object to a file"""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (pickle.PicklingError, FileNotFoundError, OSError) as e:
            print(f"Error serializing object: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file"""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (pickle.UnpicklingError, FileNotFoundError, EOFError, AttributeError, OSError) as e:
            print(f"Error deserializing object: {e}")
            return None
