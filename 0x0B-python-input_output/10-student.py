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
        if isinstance(attrs, list) and isinstance((all(attrs)), str):
            for elem in attrs:
                return elem.__dict__
        return (self).__dict__
