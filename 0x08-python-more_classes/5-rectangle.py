#!/usr/bin/python3
"""
Define class Rectangle
"""


class Rectangle:
    """Initializes square"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            string = string
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    string += "#"
                string += "\n"
            string = string[:len(string) - 1]
        return string

    def __repr__(self):
        return 'Rectangle(%s, %s)' % (self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
