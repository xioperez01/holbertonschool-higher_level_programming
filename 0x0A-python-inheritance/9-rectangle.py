#!/usr/bin/python3
"""
Module 8-rectangle.py
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class that inherits from BaseGeometry """
    def __init__(self, width, height):
        """Instantiation with width and height"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area"""
        return (self.__width) * (self.__height)

    def __str__(self):
        """prints rectangle description"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__width, self.__height)
