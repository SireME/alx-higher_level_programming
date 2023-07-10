#!/usr/bin/python3
"""
Write a class BaseGeometry (based on 5-base_geometry.py).

Public instance method: def area(self): thatraises an
    Exception with the message area() is not implemented
You are not allowed to import any module
"""


class BaseGeometry:
    """
    Raise exception on no implementation of area
    """
    def area(self):
        """
        create public intsnace method that raises an exception

        Args:
             None
        Return:
             None
        """
        raise Exception("area() is not implemented")
