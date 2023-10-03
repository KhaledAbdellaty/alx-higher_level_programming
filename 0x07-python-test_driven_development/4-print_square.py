#!/usr/bin/python3
"""Defination of print square."""


def print_square(size):
    """a function that prints
       a square with the character #.

       Raises:
             raise TypeError: size must be an integer.
             raise ValueError: if size is less than 0.
             raise TypeError: if size is a float and is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        sympol = "#"
        for _ in range(size):
            print(sympol * size)
