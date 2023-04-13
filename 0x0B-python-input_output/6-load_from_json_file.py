#!/usr/bin/python3
# 6-load_from_json_file.py
"""MODULE 7: CREATE OBJECT FROM JSON file"""
import json


def load_from_json_file(filename):
    """This function creates an a Python Object from a JSON file"""
    with open(filename) as jfile:
        return json.load(jfile)
