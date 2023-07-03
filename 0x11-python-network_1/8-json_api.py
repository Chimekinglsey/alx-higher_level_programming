#!/usr/bin/python3
"""
    This is MODULE:8
    JSON string
"""
from sys import argv
import requests

if __name__ == "__main__":
    if !argv[1]:
        letter = {'q': ""}
    letter = {'q': argv[1]}
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data=letter)
    if response.json():
        response = response.json()
        print("[{}] {}".format(response.get('id'), response.get(name)))
    elif not response.json():
        print("Not a valid JSON")
    elif response.json() is None:
        print("No result")
