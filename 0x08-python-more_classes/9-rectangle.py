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
repr() should return a string representation
of the rectangle to be able to recreate a new
                  instance by using eval() (see example below)
Public class attribute number_of_instances:
Initialized to 0
Incremented during each new instance instantiation
Decremented during each instance deletion
blic class attribute print_symbol:
Initialized to #
Used as symbol for string representation
Can be any type
Static method def bigger_or_equal(rect_1, rect_2):
         that returns the biggest rectangle based on the area
rect_1 must be an instance of Rectangle, otherwise
           raise a TypeError exception with the
            message rect_1 must be an instance of Rectangle
rect_2 must be an instance of Rectangle,
otherwise raise a TypeError exception with
the message rect_2 must be an instance of Rectangle
Returns rect_1 if both have the same area value
Class method def square(cls, size=0): that returns a
         new Rectangle instance with width == height == size
You are not allowed to import any module
"""


class Rectangle:
    """
    Define a rectangle by height and width
    """
    number_of_instances = 0  # +1 or -1 on initialisation and instance deletion
    print_symbol = "#"  # symbol for string representation of rectangle print

    def __init__(self, width=0, height=0):
        """ rectangle instantiation """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def printrec(self):
        """return string rep of rec"""
        rec = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            # convert symbol to string and use
            rec += str(self.print_symbol) * self.__width + "\n"
        return rec

    def __str__(self):
        """ print str rep of rectangle"""
        return self.printrec()[0:-1]

    def __repr__(self):
        """ expression to use with eval of rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """instance deletion message"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """return biggest rectangle based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """return new Rectangle class object with width and height same"""
        return cls(size, size)
