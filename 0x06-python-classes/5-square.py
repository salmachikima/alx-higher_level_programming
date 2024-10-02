#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square by: (based on 4-square.py).

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0):
        """it Create new instances.

        Args:
            size: of the square which is one side.
        """
        self.__size = size

    def area(self):
        """this Calculate the area of a square.

        Returns: current square area.
        """
        return self.__size ** 2

    @property
    def size(self):
        """it Returns the size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """the Property setter for size.

        Args:
            value (int): size of a square as a one side.

        Raises:
            TypeError: size must be an int
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """it prints in stdout using char #
        """

        if self.__size == 0:
            print()
        for s in range(self.__size):
            print("#" * (self.__size))
