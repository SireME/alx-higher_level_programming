#!/usr/bin/python3
"""
Write a function that prints a matrix of integers.

Prototype: def print_matrix_integer(matrix=[[]]):
Format: see example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use str.format() to print integers
"""


def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for i in matrix:
        ln = 0
        for j in i:
            lt = len(i) - 1
            print("{:d}".format(j), end=" " if ln < lt else "")
            ln += 1
        print()
