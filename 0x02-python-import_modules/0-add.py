#!/usr/bin/python3

if __name__ == "__main__":
    def add_from_another():
        import add_0
        a = 1
        b = 2
        sum = add_0.add(a, b)
        print("{:d} + {:d} = {:d}".format(a, b, sum))

    add_from_another()
