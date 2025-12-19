#!/usr/bin/python3
"""
This module contains a class and functions to manage geometric shapes.
"""


class Square():
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """This function is constructor"""
        self.size = size
        self.position = position

    def area(self):
        """This function calculate area"""
        return self.__size**2

    @property
    def size(self):
        """This function return private size"""
        return self.__size

    @size.setter
    def size(self, value):
        """This is size's setter function"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """This function return private position"""
        return self.__position

    @position.setter
    def position(self, value):
        """This is position's setter function"""
        if (not (isinstance(value, tuple) and len(value) == 2)
            and not all(isinstance(i, int) and i >= 0 for i in value)):
                raise TypeError("position must be a tuple of 2 positive integers")
        
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print("")

        for _ in range(0, self.__size):
            print(" "*self.__position[0] + "#"*self.__size) 
        
        for _ in range(self.__position[1]):
            print()
