#!/usr/bin/python3
"""MODULE: FIRST RECTANGLE: Inherits from Base class"""
from models.base import Base
from sys import argv


class Rectangle(Base):
    """This class inherits from the base class
       args:
       @width: width of rectangle
       @height: height of rectangle
       @x: x cordinate of rectangle
       @y: y cordinate of rectangle
       @id: inherited from Base class of rectangle set to None
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing our class for instance Objects"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter method for width"""
        return self.__width

    @width.setter
    def width(self, val):
        """setter method for width"""
        if type(val) is not int:
            raise TypeError("width must be an integer")
        elif val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """getter method for heigth"""
        return self.__height

    @height.setter
    def height(self, val):
        """setter method for height"""
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        elif val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """getter method for x"""
        return self.__x

    @x.setter
    def x(self, val):
        """setter method for x"""
        if type(val) is not int:
            raise TypeError("x must be an integer")
        elif val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """getter method for y"""
        return self.__y

    @y.setter
    def y(self, val):
        """setter method for y"""
        if type(val) is not int:
            raise TypeError("y must be an integer")
        elif val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """Calculates the area of rectangle"""
        return (self.width * self.height)

    def display(self):
        """Prints Rectangle instance with the character # to the stdout"""
        count = 0
        self.count = count
        [print("") for i in range(self.y)]
        [print(" ", end="") for j in range(self.x)]
        for i in range(self.height):
            [print("#", end="") for j in range(0, self.width)]
            print()
            self.count += 1
            if (self.count < self.height):
                [print(" ", end="") for j in range(self.x)]

    def __str__(self):
        """Prints [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return (str("[Rectangle] ({}) {}/{} - {}/{}\
".format(self.id, self.x, self.y, self.width, self.height)))

    def update(self, *args, **kwargs):
        """
        This method uses commandline args to assign values.
        Args:
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        """
        if args is None or len(args) <= 0:
            self.__init__(self.width,
                          self.height, self.x, self.y)
            if kwargs is None or len(kwargs) <= 0:
                return
            else:
                for k, v in kwargs.items():
                    if k == "id":
                        if v is None:
                            self.__init__(self.width,
                                          self.height, self.x, self.y)
                        else:
                            self.id = v
                    elif k == "width":
                        self.width = v
                    elif k == "height":
                        self.height = v
                    elif k == "x":
                        self.x = v
                    elif k == "y":
                        self.y = v
        else:
            argval = []
            item = 0
            arglen = len(args)
            for items in args:
                argval.append(args[-1])
            if len(args) == 1:
                self.id = argval[0]
            elif len(args) == 2:
                self.width = argval[1]
            elif len(args) == 3:
                self.height = argval[2]
            elif len(args) == 4:
                self.x = argval[3]
            elif len(args) == 5:
                self.y = argval[4]


    def to_dictionary(self):
        """returns dictionary representation of a Rectangle"""
        return {"id": self.id, "x": self.x, "y": self.y,
"height": self.height, "width": self.width}
