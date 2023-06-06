#!/usr/bin/python3

def print_ascii():
    for i in range(97, 123):
        print("{:c}".format(i), end="")


print_ascii()
