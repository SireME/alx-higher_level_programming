#!/usr/bin/python3

if __name__ == "__main__":
    def add_from_another():
        from add_0 import add
        a = 1
        b = 2
        sum = add(a, b)
        print("{:d} + {:d} = {:d}".format(a, b, sum))

    add_from_another()
