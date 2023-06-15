#!/usr/bin/python3
"""
Write a function that returns the weighted average
                of all integers tuple (<score>, <weight>)

Prototype: def weight_average(my_list=[]):
Returns 0 if the list is empty
You are not allowed to import any module
"""


def weight_average(my_list=[]):
    if len(my_list) == 0 or my_list is None:
        return 0
    product = 0
    w_sum = 0
    for iset in my_list:
        product += iset[0] * iset[1]
        w_sum += iset[1]
    return product / w_sum
