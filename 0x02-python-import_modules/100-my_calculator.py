#!/usr/bin/python3

if __name__ == "__main__":
    def math_from_another():
        from calculator_1 import add, sub, mul, div
        from sys import argv, exit

        if len(argv) != 4:
            print("Usage: {} <a> <operator> <b>".format(argv[0]))
            exit(1)

        a = int(argv[1])
        b = int(argv[3])
        operations = {"+": add, "-": sub, "*": mul, "/": div}
        if argv[2] not in operations:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

        for sign, op in operations.items():
            if sign == argv[2]:
                print("{:d} {} {:d} = {:d}".format(a, sign, b, op(a, b)))
                break

    math_from_another()
