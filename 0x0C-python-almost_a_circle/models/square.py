#!/usr/bin/python3
from models.rectangle import Rectangle
"""MODULE 10: AND NOW, THE SQUARE"""


class Square(Rectangle):
    """Inherits from rectangle class
       must be initialized to inherit all attributes of rectangle
       since a square is same as rectangle with equal w and h
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializing Square class with additional size attribute
        Args:
        @size: size of both width and height 
        @x: value of x cordinate
        @y: value of y cordinate
        @id: object integer id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns formatted output for print"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)
