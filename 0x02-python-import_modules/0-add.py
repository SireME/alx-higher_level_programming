#!/usr/bin/python3


def add_from_another():
    import add_0

    a = 1
    b = 2
    sum = add_0.add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, sum))


if __name__ == "__main__":
    add_from_another()
