#!/usr/bin/python3
'''Defination of MyList class'''


class MyList(list):
    '''MyList is subclass for list'''

    def print_sorted(self):
        '''Print sorted list'''
        print(sorted(self))
