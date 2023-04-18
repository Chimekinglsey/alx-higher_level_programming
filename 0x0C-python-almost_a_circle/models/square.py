#!/usr/bin/python3
from models.rectangle import Rectangle
"""MODULE 10: AND NOW, THE SQUARE"""


class Square(Rectangle):
    """Inherits from rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializing Square class with additional size attribute"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns formatted output for print"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)
