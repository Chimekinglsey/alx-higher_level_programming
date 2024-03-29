#!/usr/bin/python3
"""
This is MODULE:6 - This script takes in a URL + email, sends POST
request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}
    response = requests.post(url, data=email)
    print(response.text)
