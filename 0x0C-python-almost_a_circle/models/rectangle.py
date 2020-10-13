#!/usr/bin/python3
"""
Created on 12/10/2020

@author: xioperez
"""


from models.base import Base


class Rectangle(Base):
    """ class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ returns the area value of the Rectangle instance. """
        return self.__width * self.__height

    def display(self):
        """
        print the Rectangle instance with
        the character # by taking care of x and y
        """
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for m in range(self.__x):
                print(" ", end="")
            for j in range(self.__width + self.__x):
                print("#", end="")
            print()

    def __str__(self):
        return '[%s] (%d) %d/%d - %d/%d' % (self.__class__.__name__,
                                            self.id, self.__x, self.__y,
                                            self.__width, self.__height)

    def update(self, *args, **kwargs):
        """  assigns attributes """
        if args:
            i = len(args)
            if 0 in range(i):
                self.id = args[0]
            if 1 in range(i):
                self.width = args[1]
            if 2 in range(i):
                self.height = args[2]
            if 3 in range(i):
                self.x = args[3]
            if 4 in range(i):
                self.y = args[4]
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        dic = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        return dic
