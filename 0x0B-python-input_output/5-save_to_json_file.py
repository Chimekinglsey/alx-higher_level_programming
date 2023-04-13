#!/usr/bin/python3
"""Module 6: Object-to-text_file"""
import json


def save_to_json_file(my_obj, filename):
    """Saves Object to filename"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
    
