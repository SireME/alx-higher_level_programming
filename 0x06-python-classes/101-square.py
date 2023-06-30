#!/usr/bin/python3
"""
This modules conatins a class that that defines a square
"""


class Square:
    """square with initialised private instance"""

    def __init__(self, size=0, position=(0, 0)):
        """instantiate class"""
        self.size = size
        self.position = position

    def area(self):
        """determine area of square
          return:  area of a square
        """
        return (self.__size) ** 2

    def my_print(self):
        """print square to stdout using symbol#"""
        ssize = self.__size
        result = ""
        if ssize == 0:
            result += "\n"
        else:
            for i in range(self.position[1]):
                result += "\n"
            for j in range(ssize):
                result += " " * self.position[0] + "#" * ssize + "\n"
        return result

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
        else:
            self.__size = value

    @property
    def position(self):
        """get position"""
        return self.__position

    @position.setter
    def position(self, value):
        """get position"""
        if (not isinstance(value, tuple)) or (not len(value) == 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __str__(self):
        """override default print"""
        return self.my_print()[0:-1]
