#!/usr/bin/python3
"""First create a Square class to start"""


class Square:
    """Call __init__() to initialize it"""
    def __init__(self, size=0, position=(0, 0)):
        """Our code behaviour for class intances follow"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Method to return position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for position instance"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """A method to print square, if squaresize is 0, return empty line"""
        a = self.__size
        b = self.__position
        if a == 0:
            print()
        elif a > 0 and b[1] > 0:
            for size in range(a):
                # for size in (self.__position):
                for size in range(b[1]):
                    print("_", end="")
                for size in range(a):
                    print("#", end="")
                print("")
        elif a > 0 and b[1] < 1:
            for size in range(a):
                for size in range(b[0]):
                    print("_", end="")
                for size in range(a):
                    print("#", end="")
                print("")
