#!/usr/bin/env python3
"""This is python serialization module"""


import csv
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, "r", newline='') as file:
            csv_reader = csv.DictReader(file)
            data = list(csv_reader)

        with open("data.json", "w") as json_file:
            json.dump(data, json_file)
        
        return True
    except (FileNotFoundError, IOError):
        return False
