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
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string rep of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string representation of list object to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write('[]')
#            newlist = [dict(item) for item in list_objs]
            else:
                list_dicts = [item.to_dictionary() for item in list_objs]
                f.write(Base.to_json_string(list_dicts))
#            jfile = Base.to_json_string(list_dicts)
#            new_json = json.dump(jfile, f)
