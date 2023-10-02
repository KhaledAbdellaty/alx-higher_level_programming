#!/usr/bin/python3
"""Defination of Rectangle Class."""


class Rectangle:
    """The attributes and methods in Recatangle class."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
                rec_str += str(self.print_symbol) * self.__width + "\n"
            rec_str += str(self.print_symbol) * self.__width
            return rec_str

    def __repr__(self):
        """Return the string representation of the Rectangle."""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print custom message when deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_2.area() > rect_1.area():
                return rect_2
            else:
                return rect_1

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance
           with width == height == size.
        """
        return Rectangle(size, size)
