#!/bin/bash
# Send POST requests with -H parameters, the -X POST is unnecessary
curl -s -w "%{http_code}" $1 -o status_code_200_ok
