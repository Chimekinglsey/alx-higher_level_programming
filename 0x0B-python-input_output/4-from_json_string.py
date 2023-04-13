#!/usr/bin/python3
""" Module FIVE: JSON to Python Dict converter FUnction."""
import json


def from_json_string(my_str):
    """This fucntion returns the Python object represented by a JSON string"""
    return json.loads(my_str)
