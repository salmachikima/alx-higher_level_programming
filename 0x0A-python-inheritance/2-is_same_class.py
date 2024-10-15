#!/usr/bin/python3
"""Module containing is same class method"""


def is_same_class(obj, a_class):
    """Returns:
    True: if obj is exactly an instance of the specified class
    False: else"""
    return type(obj) == a_class
