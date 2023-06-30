#!/bin/bash
# Send POST requests with -H parameters
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" $1
