#!/usr/bin/python3
"""
This module contains a class and functions to manage geometric shapes.
"""


class Square():
    """Defines a square"""

    def __init__(self, size=0):
        """This function is constructor"""
        self.__size = size

    @property
    def size(self):
        "This function return private size"
        return self.__size

    @size.setter
    def size(self, value):
        "This is size's setter function"
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        "This function calculate area"
        return self.__size**2
