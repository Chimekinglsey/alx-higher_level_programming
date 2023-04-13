#!/usr/bin/python3
""" Module FOUR: JSON converter FUnction."""
import json


def to_json_string(my_obj):
    """
    This fucntion returns the JSON representation
    of a given object
    @Args: my_obj
    """
    return json.dumps(my_obj)
