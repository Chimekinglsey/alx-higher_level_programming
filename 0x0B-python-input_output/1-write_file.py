#!/usr/bin/python3
""" Module 2: Writer FUnction."""


def write_file(filename="", text=""):
    """
    This function writes a string to a text file (UTF8) 
    and returns the number of characters written
    @Args: 
    filename: Name of file to write to
    text: content to be written into file
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(text)
        return (f.tell())
