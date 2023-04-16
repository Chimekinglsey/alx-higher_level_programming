#!/usr/bin/python3
"""MODULE 11: STUDEN TO JSON WITH FILTER"""


class Student:
    """This class defines as args: student first and lastname, + age"""
    def __init__(self, first_name, last_name, age):
        """we instantiate our pubic attributes for Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves the dictionary representation of Student class"""
        if isinstance(attrs, list) and all(type(ele) == str for ele in attrs):
        #if (type(attrs) == list and
        #        all(type(ele) == str for ele in attrs)):
            return {el: getattr(self, el) for el in attrs if hasattr(self, el)}
        return self.__dict__

    def reload_from_json(self, json):
        """this method replaces all attributes of the Student instance"""
        for key, val in json.items():
            setattr(self, key, val)
