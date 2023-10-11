#!/usr/bin/python3
'''Defination of appending a text file.'''


def append_write(filename="", text=""):
    '''Appends a string to a text file.

    Args:
        filename (str): is a text file.
        text (str): the text to write.
    Return:
        returns the number of charachters appended.
    '''

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
