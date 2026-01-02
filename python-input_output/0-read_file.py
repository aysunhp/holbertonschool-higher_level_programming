#!/usr/bin/python3
"""This is input-output module"""


def read_file(filename=""):
    with open(filename, "r") as f:
        print(f.read())
