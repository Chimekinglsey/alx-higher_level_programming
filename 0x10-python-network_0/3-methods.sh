#!/bin/bash
# Display all HTTP methods the server accepts
curl -sX OPTIONS $1
