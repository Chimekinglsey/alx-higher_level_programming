#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    result = 0
    c = length - (length - 1)
    if length == 1:
        print("{}".format(0))
    elif length == 2:
        print("{}".format(int(argv[1])))
    elif length > 2:
        while (c <= length-1):
            result = result + int(argv[c])
            c = c + 1
        print("{}".format(result))
