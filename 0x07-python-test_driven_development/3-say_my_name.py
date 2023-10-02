#!/usr/bin/python3
"""Defination of say_my_name function."""


def say_my_name(first_name, last_name=""):
    """A function that prints
       My name is <first name> <last name>

       Args:
           first_name (str): The first name.
           last_name (str): The last name.

       Raise:
           raise a TypeError exception with the message
           first_name must be a string or last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
