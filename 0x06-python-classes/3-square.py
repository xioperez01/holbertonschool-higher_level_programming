#!/usr/bin/python3
"""
Module 1-square
Define class Square
"""


class Square:
    """Class for size square """
    def __init__(self, size=0):
        """ Initializes square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Calculating the area of the square"""
        return self.__size * self.__size
