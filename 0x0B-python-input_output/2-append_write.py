#!/usr/bin/python3
""" Module 3: Append FUnction."""


def append_write(filename="", text=""):
    """
    This function appends a string to the end of a text file (UTF8)
    and returns the number of characters added
    @Args:
    filename: Name of file to append to
    text: content to be added to file
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        f.seek(0, 1)
        f.write(text)
        return (f.tell())
