#!/usr/bin/python3
"""Module 1: We will create and work with Rectangle class"""


class Rectangle:
    """This will form our blue-print for rectangle objects"""
    def __init__(self, width=0, height=0):
        """This is the definition of arguments
         expected as argument from any object created"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """This method gets width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This method gets height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value for width"""
        if type(value) not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
