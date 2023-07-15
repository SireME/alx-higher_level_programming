#!/usr/bin/python3
"""
rectangle module with base inheritance
"""
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width private getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter """
        self.__width = value

    @property
    def height(self):
        """height private getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter """
        self.__height = value

    @property
    def x(self):
        """x coordinate private getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x coordinate private setter """
        self.__x = value

    @property
    def y(self):
        """y coordinate private getter"""
        return self.__y

    @width.setter
    def y(self, value):
        """y coordinate private setter """
        self.__y = value
