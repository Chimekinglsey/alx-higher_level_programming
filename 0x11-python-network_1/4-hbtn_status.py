#!/usr/bin/python3
"""
This is MODULE:0 - Using urllib
0. What's my status? #0
"""

import requests


if __name__ == "__main__":
    req_url = "https://alx-intranet.hbtn.io/status"
    fetcher = requests.get(req_url)
    content = str(fetcher.text)
    content_type = type(content)
    print("Body response:\n\t- type: {}\n\
\t- content: {}".format(content_type, content))
