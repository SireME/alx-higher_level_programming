#!/usr/bin/python3
"""
Write a function that returns True if the object
is exactly an instance of the specified class ; otherwise False.

Prototype: def is_same_class(obj, a_class):
"""


def is_same_class(obj, a_class):
    """
    check if object is an instance of the specified class

    Arg:
        obj: The object to check if it is an instance of class
        , a_class : The class to determine
    Return:
        True if the object is an instance of the class else False
    """
    return type(obj) is a_class
