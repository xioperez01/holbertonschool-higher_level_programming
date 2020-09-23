#!/usr/bin/python3
"""
Module 5-square
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
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
