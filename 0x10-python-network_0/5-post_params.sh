#!/bin/bash
# Send POST requests with -H parameters, the -X POST is unnecessary
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" $1
