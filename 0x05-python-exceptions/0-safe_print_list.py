#!/usr/bin/python3
"""
Write a function that prints x elements of a list.

Prototype: def safe_print_list(my_list=[], x=0):
my_list can contain any type (integer, string, etc.)
All elements must be printed on the same line followed by a new line.
x represents the number of elements to print
x can be bigger than the length of my_list
Returns the real number of elements printed
You have to use try: / except:
You are not allowed to import any module
You are not allowed to use len()
"""


def safe_print_list(my_list=[], x=0):
    printed = 0
    i = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            printed += 1
        except Exception as es:
            pass
        i += 1
    print()
    return printed
