#!/bin/bash
# Take an URL, send a request and get size of response in byte
curl -Is "$1" | grep Content-Length | cut -f2 -d' '
