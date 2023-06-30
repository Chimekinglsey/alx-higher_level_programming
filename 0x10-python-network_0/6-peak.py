#!/usr/bin/python3
"""Find the Peak of a given an array"""


def find_peak(list_of_integers):
    """This function takes a list, sorts it and returns the peak value"""
    sorted_list = sorted(list_of_integers)
    if len(sorted_list) > 0:
        return sorted_list[-1]
    else:
        return None
    """
    if len(list_of_integers) < 1:
        return None
    peak_val = list_of_integers[0]
    for num in list_of_integers:
        if num > peak_val:
            peak_val = num
    return peak_val
    """
