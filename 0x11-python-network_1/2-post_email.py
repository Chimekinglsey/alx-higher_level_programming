#!/usr/bin/python3
"""
This is MODULE:2 - This script takes in a URL + email, sends POST
request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
from sys import argv
from urllib import request, parse

if __name__ == "__main__":
    url = argv[1]
    email = parse.urlencode({'email': argv[2]})
    data = email.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as resp:
        decode = resp.decode('utf-8')
        display = decode.read()
        print(display)
