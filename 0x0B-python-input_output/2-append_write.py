#!/usr/bin/python3
"""
Write a function that appends a string at the end of a
text file (UTF8) and returns the number of characters added:

Prototype: def append_write(filename="", text=""):
If the file doesn’t exist, it should be created
You must use the with statement
You don’t need to manage file permission
        or file doesn't exist exceptions.
"""


def append_write(filename="", text=""):
    """
    append text at the end of a file

    Args:
         filename: name of file
         text: text to be appended
    Return:
           Number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as fl:
        characters_appended = fl.write(text)
    return characters_appended
