#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an int")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """it Get and set the current position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("the position must be a tuple of 2 + ints")
        self.__position = value

    def area(self):
        """it Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """
        it prints a square using #
        """
        if self.size == 0:
            print()
        for s in range(self.position[1]):
            print("\n")
        for s in range(self.size):
            for r in range(self.position[0]):
                print(" ", end="")
            for k in range(self.size):
                print("#", end="")
            print()
