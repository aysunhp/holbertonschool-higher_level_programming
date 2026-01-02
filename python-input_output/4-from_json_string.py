#!/usr/bin/python3
"""This is input-output module"""


import json


def from_json_string(my_str):
    """this function that returns an object (Python data structure)
    represented by a JSON string"""

    obj = json.loads(my_str)
    return obj
