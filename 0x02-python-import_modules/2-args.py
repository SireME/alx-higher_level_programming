#!/usr/bin/python3

if __name__ == "__main__":
    def print_arguements():
        from sys import argv
        ind = 1
        alen = len(argv) - 1
        arg_i = "argument" if alen == 1 else "arguments"

        print("{:d} {}{}".format(alen, arg_i, "." if alen == 0 else ":"))
        for i in argv:
            if (i == argv[0]):
                continue
            print("{:d}: {}".format(ind, i))
            ind += 1

    print_arguements()
