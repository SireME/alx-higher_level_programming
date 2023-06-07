#!/usr/bin/python3

# custom is lower
def islower(c):
    return ord(c) in range(97, 123)


# print all uppercae
def uppercase(str):
    tl = 0
    ll = len(str)
    for i in str:
        tl += 1
        upper = chr(ord(i) - 32)
        pform = upper if islower(i) else i
        print("{}".format(pform), end="" if tl < ll else "\n")
