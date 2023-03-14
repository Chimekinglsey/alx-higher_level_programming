#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order"""
    lent = len(my_list)
    for i in range(lent):
        print("{}".format(my_list[lent - 1]))
        lent -= 1
