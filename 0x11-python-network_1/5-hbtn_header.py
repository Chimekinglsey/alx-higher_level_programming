#!/usr/bin/python3
"""
This is MODULE:1 - Using urllib and sys
1. Response header value #0
"""
from sys import argv
import requests

if __name__ == "__main__":
    req = requests.get(argv[1])
    print(req.headers.get('X-Request-Id'))
