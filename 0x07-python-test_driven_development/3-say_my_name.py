#!/usr/bin/python3
"""
function that says your name
"""


def say_my_name(first_name, last_name=""):
    """
    Says your name
    first name and last name must be str or expect a TypeError
    """
    # first_name must be an integer
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    # last_name must be an integer
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
