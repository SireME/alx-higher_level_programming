#!/usr/bin/python3

# print from 0 t0 99 following specifics
def o_to_99():
    for i in range(100):
        if i != 99:
            print("{:02d}, ".format(i), end="")
        if i == 99:
            print("{:02d}".format(i))


o_to_99()
