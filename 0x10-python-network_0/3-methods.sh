#!/bin/bash
# Display all HTTP methods the server accepts
curl -sI $1 | grep Allow:
