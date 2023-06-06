#!/usr/bin/python3

# print numbers in base 10 and hex
def b10_and_hex():
    for i in range(99):
        print("{0:d} = 0x{0:x}".format(i))


b10_and_hex()
