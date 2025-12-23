#!/usr/bin/python3
"""Python inheritance module"""


def inherits_from(obj, a_class):
    """inherit from class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
