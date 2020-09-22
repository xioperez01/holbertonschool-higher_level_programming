#!/usr/bin/python3
"""
Module 3-square
Define class Square
"""


class Square:
    """Class for size square """
    def __init__(self, size=0):
        """ Initializes square"""
        self.__size = size

    def area(self):
        """Calculating the area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size * self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
