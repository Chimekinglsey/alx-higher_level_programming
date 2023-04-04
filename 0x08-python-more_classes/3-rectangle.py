#!/usr/bin/python3
"""Module 1: We will create and work with Rectangle class"""


class Rectangle:
    """This will form our blue-print for rectangle objects"""
    def __init__(self, width=0, height=0):
        """This is the definition of arguments
         expected as argument from any object created"""
        self.width = width
        self.height = height

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
        elif value == 0:
            return ("")
        self.__width = value

    @property
    def height(self):
        """This method gets height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value for width"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        elif value == 0:
            return ("")
        self.__height = value

    def area(self):
        """Returns the area of rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """ Prints a unoffical and formatted version of area"""
        if self.__width == 0 or self.__height == 0:
            return ""
        liist = []
        for i in range(self.__height):
            for j in range(self.__width):
                liist.append("#")
            liist.append('\n')
        return "".join(liist)

    def perimeter(self):
        """returns perimeter i.e 2(w * h)"""
        if self.__width == 0 or self.height == 0:
            return 0
        return (2*(self.__width + self.__height))
