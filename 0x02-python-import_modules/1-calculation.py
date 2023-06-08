#!/usr/bin/python3

if __name__ == "__main__":
    def math_from_another():
        from calculator_1 import add, sub, mul, div
        a = 10
        b = 5
        operations = {"+": add, "-": sub, "*": mul, "/": div}
        for sign, op in operations.items():
            print("{:d} {} {:d} = {:d}".format(a, sign, b, op(a, b)))

    math_from_another()
