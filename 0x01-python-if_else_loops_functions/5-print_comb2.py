#!/usr/bin/python3

# print from 0 t0 99 following specifics
def o_to_99():
    for i in range(100):
        print("{:02d}".format(i), end=", " if i < 99 else "\n")


o_to_99()
