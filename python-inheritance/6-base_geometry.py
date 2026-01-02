#!/usr/bin/python3
"""Python inheritance module"""


class BaseGeometry:
    """This is base geometry class"""

    def area(self):
        raise Exception("area() is not implemented")
