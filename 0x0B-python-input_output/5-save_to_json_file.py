#!/usr/bin/python3
"""Define a JSON file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """it Write an object to a text file using JSON representation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
