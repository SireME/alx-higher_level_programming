#!/usr/bin/python3
"""
Write a function that reads a text file
                (UTF8) and prints it to stdout:

Prototype: def read_file(filename=""):
You must use the with statement
You don’t need to manage file permission
              or file doesn't exist exceptions.
"""


def read_file(filename=""):
    """
    read text file and print result to stdout
    Args:
         filename: name of text file if
    Return:
           None
    """

    with open(filename, encoding="utf-8") as fl:
        [print(line, end="") for line in fl]
