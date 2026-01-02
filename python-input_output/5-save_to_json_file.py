#!/usr/bin/python3
"""This is input-output module"""


import json


def save_to_json_file(my_obj, filename):
    """This function that writes an Object to a text file,
    using a JSON representation"""

    with open(filename, "w") as file:
        json_obj = json.dumps(my_obj)
        file.write(json_obj)
