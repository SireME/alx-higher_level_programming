#!/usr/bin/python3
"""
Write a function that returns a new dictionary
                         with all values multiplied by 2

Prototype: def multiply_by_2(a_dictionary):
You can assume that all values are only integers
Returns a new dictionary
You are not allowed to import any module
"""


def multiply_by_2(a_dictionary):
    return dict((i, 2 * vl) for i, vl in a_dictionary.items())
