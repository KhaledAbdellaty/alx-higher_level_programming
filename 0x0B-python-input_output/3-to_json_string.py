#!/usr/bin/python3
'''Defination of JSON representation of an object function.'''
import json

def to_json_string(my_obj):
    '''Return the JSON representation of a string object.'''
    return json.dumps(my_obj)
