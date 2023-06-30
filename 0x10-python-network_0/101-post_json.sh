#!/bin/bash
# Send JSON POST requests with passed args
curl -sX POST -d @$2 $1
