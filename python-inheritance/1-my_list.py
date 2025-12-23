#!/usr/bin/python3
"""Python inheritance module"""


class MyList(list):
    """A subclass of list"""
    def print_sorted(self):
        print(sorted(self))
