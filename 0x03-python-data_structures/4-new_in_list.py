#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replace an element at given index without modifying
the original list"""
    if isinstance(my_list, list):
        lent = len(my_list)
        if idx < 0:
            return my_list.copy()
        if idx > lent - 1:
            return my_list.copy()
        else:
            copy = my_list.copy()
            copy[idx] = element
            return copy
