#!/bin/bash
# Send POST requests with -H parameters
curl -sX POST -H "email:test@gmail.com" -H "subject:I will always be here for PLD" $1
