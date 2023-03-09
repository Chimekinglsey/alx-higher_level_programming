#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    c = length - (length - 1)
    if length == 1:
        print("{} arguments.".format((c-1)))
    elif length == 2:
        print("{} argument:\n{}: {}".format(c, c, argv[1]))
    elif length > 2:
        print("{} arguments:".format(length - 1))
        while (length > 2):
            print("{}: {}".format(c, argv[c]))
            length = length - 1
            c = c + 1
        print("{}: {}".format(c, argv[c]))
