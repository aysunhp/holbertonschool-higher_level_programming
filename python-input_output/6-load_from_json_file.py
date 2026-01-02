#!/usr/bin/python3
"""This is input-output module"""


import json


def load_from_json_file(filename):
    """This function  creates an Object from a JSON file"""

    with open(filename, "r") as file:
        return json.load(file)
