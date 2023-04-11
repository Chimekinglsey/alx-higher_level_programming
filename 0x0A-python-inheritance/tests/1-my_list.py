#!/usr/bin/python3
"""Module two"""


class MyList(list):
    """This is a child class of List superclass"""
    def __init__(self):
        """We initialize our class with default self"""
        list.__init__(self)

    def print_sorted(self):
        """returns a sorted list"""
        print(sorted(self))
