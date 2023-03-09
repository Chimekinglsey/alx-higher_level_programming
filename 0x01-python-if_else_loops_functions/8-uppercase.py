#!/usr/bin/python3
# islower - a function that determines case of input string
# @c: input string to check


def uppercase(str):
    for c in str:
         if ord(c) >= 97 and ord(c) <= 122:
             c = chr(ord(c) - 32)
         print("{}".format(c), end="")
     print("")
