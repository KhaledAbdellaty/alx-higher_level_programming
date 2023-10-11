#!/usr/bin/python3
'''Defination of write to a text file.'''


def write_file(filename="", text=""):
    '''Write a string to a text file.

    Args:
        filename (str): is a text file.
        text (str): the text to write.
    Return:
        returns the number of charachters written.
    '''

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
