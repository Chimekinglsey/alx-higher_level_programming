#!/usr/bin/python3
"""Creating A Square class"""


class Square:
    """Initializing created Square class"""
    def __init__(self, size=0):
        """The codes below decides the behavior of our parameters"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif int(size) < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
