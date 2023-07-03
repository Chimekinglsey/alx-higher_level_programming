#!/usr/bin/python3
"""
    cOULD HEADER BE A PROBLEM? This is MODULE:8
    JSON string
    Author: Chime Kings
"""
from sys import argv
import requests

if __name__ == "__main__":
    if !argv[1]:
        letter = {'q': ""}
    letter = {'q': argv[1]}
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data=letter)
    try:
        json_obj = response.json()
        if len(json_obj) > 0:
            print("[{}] {}".format(json_obj.get('id'), json_obj.get('name')))
        else:
            print("Not a valid JSON")
    except Exception:
        print("No result")
