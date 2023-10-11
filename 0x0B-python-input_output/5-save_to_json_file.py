#!/usr/bin/python3
'''Defination of writes an Object to a text file function.'''
import json


def save_to_json_file(my_obj, filename):
    '''writes an object to a text file using json represetation.

    Args:
        my_obj (obj): is an object that written.
        filename (str): is the text file.
    '''
    with open(filename, "w") as f:
        return json.dump(my_obj, f)
