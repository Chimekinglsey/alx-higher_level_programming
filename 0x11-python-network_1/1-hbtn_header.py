#!/usr/bin/python3
"""
This is MODULE:1 - Using urllib and sys
1. Response header value #0
"""
from sys import argv
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as req:
        info = req.info()
        print(info.get('X-Request-Id'))
