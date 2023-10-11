#!/usr/bin/python3
'''Defination of Student class.'''


class Student:
    '''Represent a student.'''
    def __init__(self, first_name, last_name, age):
        '''Init a new student.

        Args:
            first_name (str): the first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Get a dictionary representation of the Student.

        Args:
            attrs (list): is optional attributes to represent.
        '''
        if (type(attrs) == list and
                all(type(a) == str for a in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__

    def reload_from_json(self, json):
        '''Replaces all attributes of the Student instance.'''
        for key in json:
            if hasattr(self, key):
                setattr(self, key, json[key])
