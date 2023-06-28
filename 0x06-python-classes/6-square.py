#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 5-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise
      a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError
                       exception with the message size must be >= 0
Private instance attribute: position:
property def position(self): to retrieve it
property setter def position(self, value): to set it:
position must be a tuple of 2 positiveintegers, otherwiseraise aTypeError
  exception with the message position must be a tuple of 2 positive integers
Instantiation with optional size and optional position:
                                   def __init__(self, size=0, position=(0, 0)):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self):
                   that prints in stdout the square with the character #:
if size is equal to 0, print an empty line
position should be use by using space - Don’t
                        fill lines by spaces when position[1] > 0
You are not allowed to import any module
"""


class Square:
    """square with initialised private instance"""

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        self.__position = position

    def area(self):
        """determine area of square
          return:  area of a square
        """
        return (self.__size) ** 2

    def my_print(self):
        """print square to stdout using symbol#"""
        ssize = self.__size
        if ssize == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for j in range(ssize):
                print("_" * self.position[0] + "#" * ssize)

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
        else:
            self.__position = value
