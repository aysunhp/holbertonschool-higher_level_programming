#!/usr/bin/python3
"""Python abstract module"""


class Fish():
    """This is Fish class with swim and habitat method"""
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird():
    """This is Bird class with fly and habitat method"""
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in sky")


class FlyingFish(Fish, Bird):
    """This  class is inherited from Bird and Fish classes"""
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
