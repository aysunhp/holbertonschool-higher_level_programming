#!/usr/bin/python3
"""This is input-output module"""


def write_file(filename="", text=""):
    """This function writes a string to a text file and
    return number of characters written"""

    with open(filename, "w") as file:
        file.write(text)

    return len(text)
