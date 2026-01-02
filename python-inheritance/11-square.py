#!/usr/bin/python3
"""Python inheritance module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square (Rectangle):
    """This is Square class which implemented
    from Rectangle class"""

    def __init__(self, size):
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
