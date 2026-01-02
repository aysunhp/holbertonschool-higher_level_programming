#!/usr/bin/python3
"""This is input-output module"""


def append_write(filename="", text=""):
    """This function add text to end of given file
    and return the number of characters added"""

    with open(filename, "a") as file:
        file.write(text)

    return len(text)
