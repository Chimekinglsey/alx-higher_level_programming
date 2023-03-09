#!/usr/bin/python3
# islower - a function that determines case of input string
# @c: input string to check


def uppercase(str):
    for n in range(65, 91):
        i = 0;
        if (str):
            num = ord(str[i]) + 32
            i = i + 1
            print("{}".format(chr(num), end=""))
    print()
