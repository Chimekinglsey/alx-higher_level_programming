#!/usr/bin/python3
"""
MODULE 10: AND NOW, THE SQUARE
"""
from models.rectangle import Rectangle


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

    @property
    def size(self):
        """getter method for size (width and height)"""
        return self.width

    @size.setter
    def size(self, val):
        """setter method for size (width and height)"""
        if type(val) != int:
            raise TypeError("width must be an integer")
        elif val <= 0:
            raise ValueError("width must be > 0")
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """this method allows assignment to class instance attributes"""
        if args is not None and len(args) > 0:
            arglist = []
            for item in args:
                arglist.append(args[-1])
            if len(arglist) == 1:
                self.id = arglist[0]
            elif len(arglist) == 2:
                self.size = arglist[1]
            elif len(arglist) == 3:
                self.x = arglist[2]
            elif len(arglist) == 4:
                self.y = arglist[3]
        elif kwargs is not None and len(kwargs) > 0:
            for k,v in kwargs.items():

                if k == "id":
                    if v == None:
                        self.__init__(size, size, x, y, id)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v

                elif k == "x":
                    self.x = v

                elif k == "y":
                    self.y = v

    def __str__(self):
        """
        Returns formatted output for print
        return format: [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)
