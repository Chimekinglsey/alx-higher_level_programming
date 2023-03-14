#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order"""
    if my_list is not None:
        my_list.reverse()
        lent = len(my_list)
        for i in range(lent):
            print("{}".format(my_list[i]))
