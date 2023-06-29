#!/bin/bash
# this command takes an URL, sends request to it and displays the size of the body
curl -s -w "%{size_download}" "$1"
