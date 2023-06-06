#!/usr/bin/python3

# print ascii characters except q and e
def print_ascii():
    for i in range(97, 123):
        if chr(i) == "q" or chr(i) == "e":
            continue

        print("{:c}".format(i), end="")


print_ascii()
