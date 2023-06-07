#!/usr/bin/python3

# custom is lower
def islower(c):
    return ord(c) in range(97, 123)


# print all uppercae
def uppercase(str):
    for i in str:
        upper = chr(ord(i) - 32)
        print("{}".format(upper if islower(i) else i), end="")
    print()
