#!/usr/bin/python3
"""Defination of Square class."""


class Square:
    """A Square class."""
    def __init__(self, size=0):
        """Initialize new Square.

        Args:
            size (int): The size of the Square.
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Return the area of the Square."""
        return self.__size ** 2
