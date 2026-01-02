#!/usr/bin/python3
"""This is input-output module"""


def read_file(filename=""):
    """This function reads a text file and print it"""

    with open(filename, "r") as f:
        print(f.read())
