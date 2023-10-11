#!/usr/bin/python3
'''Defination of read file function'''


def read_file(filename=""):
    '''Prints the content of the file.

    Args:
        filename (str): is a  file name.'''

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
