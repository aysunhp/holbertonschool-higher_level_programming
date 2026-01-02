#!/usr/bin/python3
"""Python abstract module"""


class SwimMixin():
    """This is SwimMixin mixin with swim method"""
    def swim(self):
        print("The creature swims!")


class FlyMixin():
    """This is FlyMixin mixin with fly method"""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """This class is inherited from SwimMixin and FlyMixin mixins"""
    def roar(self):
        print("The dragon roars!")
