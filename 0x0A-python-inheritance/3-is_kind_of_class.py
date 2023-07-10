#!/usr/bin/python3
"""
Write a function that returns True if the
      object is an instance of, or if the object is an
      instance of a class that inherited from, the
      specified class ; otherwise False.

Prototype: def is_kind_of_class(obj, a_class):
"""


def is_kind_of_class(obj, a_class):
    """
    check if object is an instance of the specified classor inherited class

    Arg:
        obj: The object to check if it is an instance of class
        , a_class : The class to determine
    Return:
        True if the object is an instance of the class or inherited else False
    """
    return isinstance(obj, a_class)
