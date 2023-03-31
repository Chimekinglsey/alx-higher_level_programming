#!/usr/bin/python3

"""Creating a Square class with int size"""


class Square:
    """Initializing Private Size and ValueError if size is not int"""
    def __init__(self, size=0):
        """initializing square parameters"""
        if type(size)is not int:
               raise TypeError("size must be an integer")
        elif int(size) < 0:
            raise  ValueError("size must be >= 0")
        self.__size = size
