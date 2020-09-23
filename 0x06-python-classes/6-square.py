#!/usr/bin/python3
"""
Module 5-square
Define class Square
"""


class Square:
    """Class for size square """
    def __init__(self, size=0, position=(0, 0)):
        """ Initializes square"""
        self.__size = size
        self.__position = position

    def area(self):
        """Calculating the area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2 or \
           type(value[0]) != int or type(value[1]) != int or \
            value[0] < 0 or value[1] != 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size + self.__position[0]):
                    print("#", end="")
                print()
