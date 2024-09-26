#!/usr/bin/env python3

"""Defines classes representing different animals and their behaviors."""


class Fish:
    """Represents a fish, capable of swimming."""

    def swim(self):
        """Simulates the swimming action of the fish."""
        print("The fish is swimming")

    def habitat(self):
        """Describes the natural habitat of the fish."""
        print("The fish lives in water")


class Bird:
    """Represents a bird, capable of flying."""

    def fly(self):
        """Simulates the flying action of the bird."""
        print("The bird is flying")

    def habitat(self):
        """Describes the natural habitat of the bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish, capable of both swimming and flying."""

    def fly(self):
        """Simulates the flying action of the flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Simulates the swimming action of the flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Describes the unique habitat of the flying fish,
        which includes both water and the sky.
        """
        print("The flying fish lives both in water and the sky!")
