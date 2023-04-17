#!/usr/bin/python3
"""MODULE 1: BASE CLASS"""


class Base:
    """This will serve as base class for all other classes in this project"""
    __nb_objects = 0
    def __init__(self, id=None):
        """
           This is class constructor that initializes every
           instance of the base class
        """
        if id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects 
        else:
            self.id = id
