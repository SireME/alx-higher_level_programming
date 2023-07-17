#!/usr/bin/python3
"""
This rectangle module inherites from the base class and contains methods for
computings regarding a dictionary object
"""
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialise rectangle attributes
        and inherite as well as initialise from super class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """return width of rectangel private getter
        Args:
             None
        Return:
               width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of rectangle attribute width setter
        Args:
             value: width of rectangle
        Return:
               None
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """return width of rectangel private getter
        Args:
             None
        Return:
               width of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of rectangle attribute height setter
        Args:
             value: value of rectangle
        Return:
               None
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returning coordinate for x-axis private getter
        Args:
             None
        Return:
               x cordinate for rectangle plotting
        """
        return self.__x

    @x.setter
    def x(self, value):
        """x coordinate setting private setter
        Args:
             value: cordinate value
        Return:
               None
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y coordinate private getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y coordinate setting private setter
        Args:
             value: cordinate value
        Return:
               None
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ public method to compute the area of traingle
        Args:
             None
        Return:
               area of triangle
        """
        return self.width * self.height

    def display(self):
        """ print rectangle instance with x and y coordinates
        using # character
        Args:
             None
        Return:
               None
        """
        print("\n" * self.y, end="")
        for i in range(0, self.height):
            print(" " * self.x, end="")
            print("#" * self.width + "\n", end="")

    def update(self, *args, **kwargs):
        """update instance attributes using keyword and
        none keyword arguments
        Args:
             args: non keyworded variadic list
             kwargs: keyworded list of dictionary
        Return:
               None
        """
        if args and len(args) >= 1:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) == 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of rectangle
        Args:
             None
        Return:
               dictionary representing rectangle attributes
        """
        dic_rep = {}
        dic_rep["id"], dic_rep["width"] = self.id, self.width
        dic_rep["height"], dic_rep["x"] = self.height, self.x
        dic_rep["y"] = self.y
        return dic_rep

    def __str__(self):
        """overide str method with Rectangle parameters
        Args:
             None
        Return:
               __str__ string representation of dictionary
        """
        w = self.width
        h = self.height
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {w}/{h}"
