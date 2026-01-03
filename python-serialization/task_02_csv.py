#!/usr/bin/env python3
"""This is python serialization module"""


import csv
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, "r", newline='') as file:
            cvs_reader = csv.DictReader(file)
            for row in csv_reader:
                with open("data.json", "a") as f:
                    json.dump(row, f)
    except (FileNotFoundError, IOError):
        return False
    finally:
        return True
