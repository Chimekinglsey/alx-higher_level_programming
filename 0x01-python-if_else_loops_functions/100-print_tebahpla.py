#!/usr/bin/python3
x = range(90, 64, -1)
for n in x:
    if n % 2 == 0:
        n = n + 32
    print("{}".format(chr(n)), end='')
