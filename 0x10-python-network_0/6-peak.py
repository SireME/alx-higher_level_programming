#!/usr/bin/python3
"""
Write a function that finds a peak in a list of unsorted integers.

Prototype: def find_peak(list_of_integers):
You are not allowed to import any module
Your algorithm must have the lowest complexity
(hint: you don’t need to go through all numbers to find a peak)
6-peak.py must contain the function
6-peak.txt must contain the complexity of your
algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2)
"""


def find_peak(list_of_integers):
    """
    function to find a peak in a list of unsorted integers
    """
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # conditional left move
            right = mid
        else:
            # Otherwise, move right.
            left = mid + 1

    return list_of_integers[left]
