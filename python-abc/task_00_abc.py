#!/usr/bin/python3
"""Python abstract module"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """This is abstract Animal class"""

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """This is Dog class which implemented
    abstract Animal class"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """This is Cat class which implemented
    abstract Animal class"""
    def sound(self):
        return "Meow"
