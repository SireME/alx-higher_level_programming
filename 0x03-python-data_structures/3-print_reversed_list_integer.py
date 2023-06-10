#!/usr/bin/python3
"""

  Write a function that prints all integers of a list, in reverse order.

  Prototype: def print_reversed_list_integer(my_list=[]):
  Format: one integer per line. See example
  You are not allowed to import any module
  You can assume that the list only contains integers
  You are not allowed to cast integers into strings
  You have to use str.format() to print integers
"""


def print_reversed_list_integer(my_list=[]):
    idx = len(my_list) - 1
    for i in my_list:
        print("{:d}".format(my_list[idx]))
        idx -= 1
