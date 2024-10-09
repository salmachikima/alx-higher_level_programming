#!/usr/bin/python3
"""Define locked class"""


class LockedClass:
    """
    it Prevent user from instantiating new LockedClass attributes
    for anything but only from attributes that  called 'first_name'
    """

    __slots__ = ["first_name"]
