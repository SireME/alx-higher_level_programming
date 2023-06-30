#!/usr/bin/python3
"""
This modules contains a class that defines a square with comparison
capabilities
"""


class Square:
    """square with initialised private instance"""

    def __init__(self, size=0):
        """instantiate class"""
        self.size = size

    def area(self):
        """determine area of square
          return:  area of a square
        """
        return self.__size ** 2

    @property
    def size(self):
        """ retrieve size of square
            return : szie of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """set value new square value to instance
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def __lt__(self, other):
        """Less than comparison"""
        return self.area() < other.area()

    def __gt__(self, other):
        """Greater than comparison"""
        return self.area() > other.area()

    def __le__(self, other):
        """Less than or equal to comparison"""
        return self.area() <= other.area()

    def __ge__(self, other):
        """Greater than or equal to comparison"""
        return self.area() >= other.area()
