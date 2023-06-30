#!/usr/bin/python3
"""Find the Peak of a given an array"""


def find_peak(list_of_integers):
    """This function takes a list, sorts it and returns the peak value"""
    sorted_list = sorted(list_of_integers)
    if len(sorted_list) > 0:
        return sorted_list[-1]
    else:
        return None
