'''
Created on 12/10/2020

@author: xioperez
'''

from models.base import Base


class Rectangle(Base):
    '''
    class Rectangle
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Constructor
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def get_width(self):
        return self.__width

    @property
    def get_height(self):
        return self.__height

    @property
    def get_x(self):
        return self.__x

    @property
    def get_y(self):
        return self.__y

    def set_width(self, value):
        self.__width = value

    def set_height(self, value):
        self.__height = value

    def set_x(self, value):
        self.__x = value

    def set_y(self, value):
        self.__y = value
