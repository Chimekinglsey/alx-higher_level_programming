#!/usr/bin/python3
"""MODULE 1: BASE CLASS"""
import json


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

    def to_json_string(list_dictionaries):
        """returns JSON string rep of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        string = json.dumps(list_dictionaries)
        return string
