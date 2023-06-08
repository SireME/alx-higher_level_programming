#!/usr/bin/python3

# Import function
import add_0


def add_from_another():
    a = 1
    b = 2
    sum = add_0.add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, sum))


add_from_another()
