#!/usr/bin/python3
"""This is MODULE:0 - Using urllib"""

import urllib.request


if __name__ == "__main__":
    req = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(req) as resp:
        content = resp.read()
        utf8_content = content.decode('UTF-8')
        content_type = type(content)
    print("Body response:\n\t - type: {}\n\t - co\
ntent: {}\n\t - utf8 content: \
{}".format(content_type, content, utf8_content))


    
