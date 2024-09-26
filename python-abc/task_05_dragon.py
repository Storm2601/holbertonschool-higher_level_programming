#!/usr/bin/env python3

"""Defines mixin classes for swimming and flying behaviors and a Dragon class."""


class SwimMixin:
    """Provides swimming capability to a class."""

    def swim(self):
        """Simulates the swimming action of a creature."""
        print("The creature swims!")


class FlyMixin:
    """Provides flying capability to a class."""

    def fly(self):
        """Simulates the flying action of a creature."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represents a dragon, capable of swimming, flying, and more."""

    def roar(self):
        """Simulates the dragon's roaring action."""
        print("The dragon roars!")

    def spit_fire(self):
        """Simulates the dragon's fire-breathing ability."""
        print("The dragon spits fire!")

    def observe(self):
        """Simulates the dragon observing its surroundings."""
        print("The dragon observes!")

    def attack(self):
        """Simulates the dragon attacking."""
        print("The dragon attacks!")
