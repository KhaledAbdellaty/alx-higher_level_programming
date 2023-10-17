#!/usr/bin/python3
'''Defination of a Base Class.'''
import json


class Base:
    '''That will be parent of all the models.

    Private Class Attributes:
        __nb_objects (int): Number of instances of the Base class.
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Init a new instance from Base class.

        Args:
            id (int): The Identfier number of the instance.
        '''
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Returns JSON string from a list of dictionaries

        Args:
            list_dictionaries (list): Is a list of dictionaries

        Returns:
            if list_dictionaries is Empty or None, "[]",
            Otherwise, return JSON string representation of list_dictionaries.
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Create and writes the JSON string
        representation of list_objs to a file.

        Args:
            list_objs (list) : Is a list of inherited instances.
        '''
        if list_objs is None:
            list_objs = []
        file_name = cls.__name__ + ".json"
        json_string = \
            cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(file_name, "w") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        '''Returns the list of the JSON string representation json_string.

        Args:
            json_string (str) : A JSON String

        Returns:
            If json_string is None or empty, return an empty list
            Otherwise, return the list represented by json_string
        '''
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if dictionary is not None and dictionary != {}:
            if cls.__name__ == "Square":
                obj = cls(1)
            else:
                obj = cls(1, 1)

            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        '''Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        '''
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
