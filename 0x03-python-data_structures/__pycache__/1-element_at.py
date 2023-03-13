#!/usr/bin/python3
def element_at(my_list, idx):
<<<<<<< HEAD
    if my_list is not None and idx is not None:
=======
    if my_list != None and idx != None:
>>>>>>> b3d9c45235c2d806a0829130a0e1f9133f62782c
        lent = len(my_list) - 1
        if idx < 0 or idx > lent:
            return (None)
    value = my_list[idx]
    return value
