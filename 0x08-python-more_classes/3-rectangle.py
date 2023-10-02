#!/usr/bin/python3
"""Defination of Rectangle Class."""


class Rectangle:
    """The attributes and methods in Recatangle class."""

    def __init__(self, width=0, height=0):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for the width attribute."""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute.

           Args:
               value (int): the new value to the width
           Raise:
               raising TypeError if the argument is not int.
               raising ValueError if the argument is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute."""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute.

           Args:
               value (int): the new value to the width
           Raise:
               raising TypeError if the argument is not int.
               raising ValueError if the argument is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Retuns string that represent the rectangle using '#'."""

        rec_str = ""
        if self.__width == 0 or self.__height == 0:
            return rec_str
        else:
            for _ in range(self.__height - 1):
                rec_str += "#" * self.__width + "\n"
            rec_str += "#" * self.__width
            return rec_str
