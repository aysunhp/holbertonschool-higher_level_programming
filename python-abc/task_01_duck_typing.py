#!/usr/bin/python3
"""Python abstract module"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """This is an abstract Shape class with abstract
    area and perimeter methods"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """This  Circle class is inhereted from abstract
    Shape class"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """This Ractangle class is inhereted from abstract
    Shape class"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(item):
    """Print area and perimeter of any shape (duck typing)"""
    print(f"Area: {item.area()}")
    print(f"Perimeter: {item.perimeter()}")
