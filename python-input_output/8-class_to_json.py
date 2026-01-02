#!/usr/bin/python3
"""This is input-output module"""


import json


def class_to_json(obj):
    """This function returns the dictionary description with
    simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object"""
    json_str = json.dumps(obj.__dict__)
    return json_str
