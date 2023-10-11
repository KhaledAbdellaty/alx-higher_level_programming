#!/usr/bin/python3
'''Defination of MyList class'''


class MyList(list):
    '''MyList is subclass for list'''
    def __init__(self):
        '''init new instance.'''
        super().__init__()

    def print_sorted(self):
        '''Print sorted list'''
        print(sorted(self))
