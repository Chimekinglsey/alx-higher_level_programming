#!/usr/bin/python3
"""First create a Square class"""


class Square:
    """Call __init__() to initialize it"""
    def __init__(self, size=0):
        """Our code behaviour for class intances follow"""
        self.__size = size

    def area(self):
        """This method returns size ** 2"""
        return self.__size * self.__size

    @property
    def size(self):
        """This method gets the size value passed to setter"""
        return self.__size

    @size.setter
    def size(self, value):
        """This method sets size values"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """A method to print square, if squaresize is 0, return empty line"""
        a = self.__size
        if a == 0:
            print()
        else:
            for size in range(a):
                for size in range(a):
                    print("#", end="")
                print()
