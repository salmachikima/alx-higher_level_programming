#!/usr/bin/python3
"""Defines int addition function"""


def add_integer(a, b=98):
    """Return the int add of a & b

    before addition is performed Float arguments are typecasted to ints

    Raises
        TypeError: If either of a or b is a non-int and non-float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
