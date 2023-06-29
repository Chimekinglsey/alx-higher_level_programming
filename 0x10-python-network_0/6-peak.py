#!/usr/bin/python3
"""
MODULE 6: FIND A PEAK: Technical interview preparation
A function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Return the peak in a list of integers
    """
    if len(list_of_integers) > 0:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
