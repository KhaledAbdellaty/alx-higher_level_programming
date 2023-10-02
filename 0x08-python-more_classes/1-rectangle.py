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
