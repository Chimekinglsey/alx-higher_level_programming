#!/usr/bin/python3
""" Module One: File Reader FUnction."""


def read_file(filename=""):
    """
    this function reads a textfile and prints it
    @Args: filename
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
