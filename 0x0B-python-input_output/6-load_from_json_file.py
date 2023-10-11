#!/usr/bin/python3
'''Defination of create an Object from a JSON file.'''
import json


def load_from_json_file(filename):
    '''Creates an Object from a "JSON file".

    Args:
        filename (str): is the JSON file.
    Return:
        returns an Object.
    '''
    with open(filename) as f:
        return json.load(f)
