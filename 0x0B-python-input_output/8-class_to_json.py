#!/usr/bin/python3
"""MODULE 9: returns Dictionary description"""


def class_to_json(obj):
    """a function that returns the dictionary description with simple data
    data structure like list, dictionary etc"""
    return obj.__dict__
