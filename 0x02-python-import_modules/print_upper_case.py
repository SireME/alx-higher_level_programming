#!/usr/bin/python3

def print_ascii():
    for i in range(97, 123):
        print("{:c}".format(i - 32), end="" if i < 122 else "\n")


print_ascii()
