#!/usr/bin/python3
"""Defines a string-to-JSON function"""
import json


def to_json_string(my_obj):
    """Return JSON representation of a str obj"""
    return json.dumps(my_obj)
