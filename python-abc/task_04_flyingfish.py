#!/usr/bin/python 3
"""class that inherits from both a Fish class and a Bird """


class Fish:
    """class fish with swim method"""
    def swim(self):
        """print The fish is swimming"""
        print("The fish is swimming")

    def habitat(self):
        """print The fish lives in water"""
        print("The fish lives in water")


class Bird:
    """class bird with fly and habitat method"""
    def fly(self):
        """print The bird is flying"""
        print("The bird is flying")

    def habitat(self):
        """print The bird lives in the sky"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class flying fish"""

    def swim(self):
        """Overrides swim method"""
        print("The flying fish is swimming!")

    def fly(self):
        """Overrides fly method"""
        print("The flying fish is soaring!")

    def habitat(self):
        """Overrides habitat method"""
        print("The flying fish lives both in water and the sky!")
