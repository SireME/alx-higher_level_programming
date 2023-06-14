#!/usr/bin/python3
"""
Technical interview preparation:

You are not allowed to google anything
Whiteboard first
Create a function def roman_to_int(roman_string):
              that converts a Roman numeral to an integer.

You can assume the number will be between 1 to 3999.
def roman_to_int(roman_string) must return an integer
If the roman_string is not a string or None, return 0
"""


def roman_to_int(roman_string):
    rs = roman_string
    # make sure input is a string and not empty
    if rs is None or isinstance(rs, str) is False:
        return 0

    # getting input roman numeral string to corresponding number
    romann = {"I":1, "V":5, "X":10, "L":50 , "C":100, "D":500, "M":1000}
    number = []
    for i in rs:
        for k in romann.keys():
            if i.lower() == k.lower():
                number.append(romann[k])
                break

    # logic for conversion
    arabic_n = 0
    i = 0
    while i < len(number) - 1:
        if number[i + 1] > number[i]:
            arabic_n -= number[i]
        else:
            arabic_n += number[i]
        i += 1
    arabic_n += number[-1]

    return arabic_n
