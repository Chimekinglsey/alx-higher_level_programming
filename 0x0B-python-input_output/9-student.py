#!/usr/bin/python3
"""MODULE 10: STUDEN TO JSON CLASS"""


class Student:
    """This class defines a student first and lastname, + age"""
    def __init__(self, first_name, last_name, age):
        """we instantiate our pubic attributes for Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves the dictionary representation of Student class"""
        return (self).__dict__
