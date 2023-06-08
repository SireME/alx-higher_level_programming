#!/usr/bin/python3

if __name__ == "__main__":
    def sum_all():
        from sys import argv
        sumall = 0

        for i in argv:
            if (i == argv[0]):
                continue
            sumall += int(i)
        print(sumall)

    sum_all()
