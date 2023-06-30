#!/bin/bash
# This takes a URL, sends GET request to it and displays the body of the response following all redirects
curl -sL $1
