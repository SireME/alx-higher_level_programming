#!/usr/bin/python3
"""
Write a class Rectangle that defines a
             rectangle by: (based on 0-rectangle.py)

Private instance attribute: width:
property def width(self): to retrieve it
property setter def width(self, value): to set it:
width must be an integer, otherwise raise a TypeError
        exception with the message width must be an integer
if width is less than 0, raise a ValueError
                exception with the message width must be >= 0
Private instance attribute: height:
property def height(self): to retrieve it
property setter def height(self, value): to set it:
height must be an integer, otherwise raise a
    TypeError exception with the message height must be an integer
if height is less than 0, raise a ValueError
              exception with the message height must be >= 0
Instantiation with optional width and height:
                    def __init__(self, width=0, height=0):
Public instance method: def area(self):
                          that returns the rectangle area
Public instance method: def perimeter(self):
              that returns the rectangle perimeter:
if width or height is equal to 0, perimeter is equal to 0
You are not allowed to import any module
"""


class Rectangle:
    """
    Define a rectangle by height and width
    """
    def __init__(self, width=0, height=0):
        """ rectangle instantiation """
        self.width = width
        self.height = height

    @property
    def width(self):
        """return width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ return the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
