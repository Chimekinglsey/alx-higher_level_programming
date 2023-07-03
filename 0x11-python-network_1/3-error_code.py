#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""
from sys import argv
from urllib import request, error

if __name__ == "__main__":
    try:
        url = argv[1]
        with request.urlopen(url) as resp:
            display = resp.read().decode('utf-8')
            print(display)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
