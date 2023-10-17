#!/usr/bin/python3
'''Defination of a Rectangle class That inherit from Base Class.'''
from models.base import Base


class Rectangle(Base):
    '''A Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Init a new instance from Rectangle class.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The Identfier number of the new Rectangle.
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''get the width of the Rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set a new value to width the private attribute.

        Args:
            value (int) : the new value.

        Raises:
            TypeError : if value is not int type.
            ValueError: if value is less than 1.
        '''
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''get the height of the Rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set a new value to height the private attribute.

        Args:
            value (int) : the new value.

        Raises:
            TypeError : if value is not int type.
            ValueError: if value is less than 1.
        '''
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        '''Get the x coordinate of the Rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Set a new value to x the private attribute.

        Args:
            value (int) : the new value.

        Raises:
            TypeError : if value is not int type.
            ValueError: if value is less than 1.
        '''
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        '''Get the y coordinate of the Rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Set a new value to y the private attribute.

        Args:
            value (int) : the new value.

        Raises:
            TypeError : if value is not int type.
            ValueError: if value is less than 1.
        '''
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        '''Return the area of the Rectangle.'''
        return self.height * self.width

    def display(self):
        '''Print the Rectangle using the (#) character.'''
        [print() for z in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for z in range(self.x)]
            for x in range(1, self.width):
                print("#", end="")

            print("#")

    def __str__(self):
        '''Return the print() and str() representation of the Rectangle.'''
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        '''Update the Rectangle using “no-keyword argument” or\
            “key-worded argument”.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        '''
        flag = 0
        if len(args) != 0:
            for i in range(len(args)):
                if (flag == 0):
                    if args[0] is None:
                        self.__init__(self.width,  self.height, self.x, self.y)
                    else:
                        self.id = args[i]
                elif (flag == 1):
                    self.width = args[i]
                elif (flag == 2):
                    self.height = args[i]
                elif (flag == 3):
                    self.x = args[i]
                elif (flag == 4):
                    self.y = args[i]
                flag += 1

        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        '''Return the dictionary representation of a Rectangle.'''
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
                }
