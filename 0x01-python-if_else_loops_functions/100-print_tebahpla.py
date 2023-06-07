#!/usr/bin/python3

def print_rev_ascii():
    cap = 1
    for i in range(122, 96, -1):
        print("{:c}".format(i - 32 if cap % 2 == 0 else i), end="")
        cap += 1


print_rev_ascii()
