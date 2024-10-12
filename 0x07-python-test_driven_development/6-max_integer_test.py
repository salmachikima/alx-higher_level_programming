#!/usr/bin/python3
"""
 find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        the list is empty returns nada
    """
    if len(list) == 0:
        return None
    result = list[0]
    s = 1
    while s < len(list):
        if list[s] > result:
            result = list[s]
        s += 1
    return result


