#!/usr/bin/python3

from sys import argv

with open('NewCommand.txt', 'a') as f:
	f.write(str(argv[1:])
