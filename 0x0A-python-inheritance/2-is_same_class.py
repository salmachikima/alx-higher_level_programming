#!/usr/bin/python3
"""2-is_same_class.py
"""


def is_same_class(obj, a_class):
    """ True if the object is exactly an instance of the specified class
else False """
    return type(obj) == a_class
