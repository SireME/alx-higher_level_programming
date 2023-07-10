#!/usr/bin/python3
"""
Write a function that returns True if the object is an instance of
         a class that inherited (directly or indirectly) from the
          specified class ; otherwise False.

Prototype: def inherits_from(obj, a_class):
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a class that inherited
    (directly or indirectly)
    from the specified class, otherwise False.

    Args:
        obj: object to check
        a_class: class to check

    Returns:
        True if obj is an instance of a class that inherited from a_class,
        otherwise False
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
