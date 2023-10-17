#!/usr/bin/python3
'''Defination of a Square class That inherit from Rectangle Class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''A Square class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Init a new instance from Square class.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The Identfier number of the new Square.
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Return the print() and str() representation of the Square.'''
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''get the size of the Square.'''
        return self.width

    @size.setter
    def size(self, value):
        '''Set a new value to the Square size.

        Args:
            value (int) : the new value.
        '''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Update the Square using “no-keyword argument”\
            or “key-worded argument”.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3th argument represents x attribute
                - 4th argument represents y attribute
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
                    self.size = args[i]
                elif (flag == 2):
                    self.x = args[i]
                elif (flag == 3):
                    self.y = args[i]
                flag += 1

        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        '''Return the dictionary representation of a Square.'''
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
                }
