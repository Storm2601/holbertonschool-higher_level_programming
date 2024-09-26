#!/usr/bin/python3

"""
Defines an abstract method in an abstract class inherited from ABC.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Represents an abstract class that inherits from ABC.
    Contains an abstract method `sound` that must be implemented by subclasses.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses.
        Should return the sound made by the animal.
        """
        pass


class Dog(Animal):
    """
    A subclass of Animal representing a dog.
    Implements the `sound` method to return the sound a dog makes.
    """

    def sound(self):
        """Returns the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """
    A subclass of Animal representing a cat.
    Implements the `sound` method to return the sound a cat makes.
    """

    def sound(self):
        """Returns the sound of a cat."""
        return "Meow"
