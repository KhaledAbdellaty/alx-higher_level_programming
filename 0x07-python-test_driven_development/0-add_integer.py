#!/usr/bin/python3

"""
   add integer function


"""


def add_integer(a, b=98):
    """Return the sum of a and b.
       Raises:
           TypeError: if the arguments are not integer or float."""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
