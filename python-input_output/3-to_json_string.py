#!/usr/bin/python3
"""This is input-output module"""


import json


def to_json_string(my_obj):
    """this function  returns the JSON representation of an object (string)"""

    json_str = json.dumps(my_obj)
    return json_str
