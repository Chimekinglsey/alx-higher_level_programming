#!/usr/bin/python3
def element_at(my_list, idx):
    if my_list != None and idx != None:
        lent = len(my_list) - 1
        if idx < 0 or idx > lent:
            return (None)
    value = my_list[idx]
    return value
