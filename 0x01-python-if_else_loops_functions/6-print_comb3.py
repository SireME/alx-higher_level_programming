#!/usr/bin/python3

# print all possible digit combinations
def comb_two():
    for i in range(10):
        for j in range(i+1, 10):
            if (i * 10 + j) == 89:
                print(89)
                break
            print("{:02d}".format(i * 10 + j), end=", ")


comb_two()
