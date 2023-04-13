#!/usr/bin/python3
import json
""" Module FOUR: JSON converter FUnction."""


def to_json_string(my_obj):
    """
    This fucntion returns the JSON representation
    of a given object
    @Args: my_obj
    """
    return json.dumps(my_obj)
