#!/usr/bin/python3

# print last digit of a number
def print_last_digit(number):
    if number < 0:
        number = -1 * number
    return number % 10
