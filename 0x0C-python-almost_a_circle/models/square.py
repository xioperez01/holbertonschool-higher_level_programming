#!/usr/bin/python3
"""
Created on 12/10/2020

@author: xioperez
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return '[%s] (%d) %d/%d - %d' % (self.__class__.__name__,
                                         self.id, self.x, self.y, self.size)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """  assigns attributes """
        if args:
            i = len(args)
            if 0 in range(i):
                self.id = args[0]
            if 1 in range(i):
                self.size = args[1]
            if 2 in range(i):
                self.x = args[2]
            if 3 in range(i):
                self.y = args[3]
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ returns the dictionary representation of a Square """
        dic = {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }
        return dic
