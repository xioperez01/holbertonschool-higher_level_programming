#!/usr/bin/python3
"""
Module 5-base_geometry
"""


class BaseGeometry():
    """Class"""
    def area(self):
        """ Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value < 0 or value == 0:
            raise ValueError("{:s} must be greater than 0".format(name))


"""
Module 8-rectangle.py
"""


class Rectangle(BaseGeometry):
    """ Class that inherits from BaseGeometry """
    def __init__(self, width, height):
        """Instantiation with width and height"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
