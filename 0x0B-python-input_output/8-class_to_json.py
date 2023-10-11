#!/usr/bin/python3
'''Defination a Python class-to-JSON function.'''


def class_to_json(obj):
    '''Return the dictionary description with simple data structure.'''
    return obj.__dict__
