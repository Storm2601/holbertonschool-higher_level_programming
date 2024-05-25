#!/usr/bin/ptyhon3
"""Design two mixin classes
Show that a Dragon instance can both swim and fly"""


class SwimMixin:
    """swim class"""
    def swim(self):
        """print"""
        print("The creature swims!")


class FlyMixin:
    """fly class"""
    def fly(self):
        """print The creature flies!"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """mix class fly and swim"""
    def roar(self):
        """print The dragon roars!"""
        print("The dragon roars!")

    def scratch(self):
        """print the dragon scratch your face!"""
        print("the dragon scratch your face!")

    def moonwalk(self):
        """print the dragon does the moonwalk in front of you Oo"""
        print("the dragon does the moonwalk in front of you Oo")
