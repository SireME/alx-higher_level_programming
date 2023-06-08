#!/usr/bin/python3

# Import function
from add_0 import add


def add_from_another():
    a = 1
    b = 2
    sum = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, sum))


add_from_another()
