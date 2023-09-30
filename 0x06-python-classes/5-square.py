#!/usr/bin/python3
"""Defination of Square class."""


class Square:
    """A Square class."""
    def __init__(self, size=0):
        """Initialize new Square.

        Args:
            size (int): The size of the Square.
        """
        self.size = size

    @property
    def size(self):
        """Get the size value."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set value to size attribute."""
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """prints in stdout the square with the character '#'."""
        if self.size > 0:
            for i in range(self.size):
                for x in range(self.size):
                    print("#", end="")
                print("#")
        else:
            print()

    def area(self):
        """Return the area of the Square."""
        return self.__size ** 2
