#!/usr/bin/python3
""" Module FIVE: JSON to Python Dict converter FUnction."""
import json


def to_json_string(my_obj):
    """
    This fucntion returns the Python object represented by a JSON string
    """
    return(json.loads(my_obj))
