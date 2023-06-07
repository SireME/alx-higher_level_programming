#!/usr/bin/python3

# print last digit of a number
def print_last_digit(number):
    if number < 0:
        number = -1 * number
    print(number % 10, end="")
    return number % 10
