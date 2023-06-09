#!/usr/bin/python3
"""
Write a function that finds the biggest integer of a list.

Prototype: def max_integer(my_list=[]):
If the list is empty, return None
You can assume that the list only contains integers
You are not allowed to import any module
You are not allowed to use the builtin max()
"""


def max_integer(my_list=[]):
    return "None" if len(my_list) == 0 else sorted(my_list)[-1]
