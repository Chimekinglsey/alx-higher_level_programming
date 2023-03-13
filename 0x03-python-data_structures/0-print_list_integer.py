#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if my_list is not None:
        lent = len(my_list)
        lent2 = lent - (lent - 1)
        while (lent > 0):
            print("{}".format(my_list[lent2 - 1]))
            lent -= 1
            lent2 += 1
