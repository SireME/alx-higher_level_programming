#!/usr/bin/python3
"""
Write a function that writes a string to a text
file (UTF8) and returns the number of characters written:

Prototype: def write_file(filename="", text=""):
You must use the with statement
You don’t need to manage file permission exceptions.
Your function should create the file if doesn’t exist.
Your function should overwrite the content
                       of the file if it already exists.
"""


def write_file(filename="", text=""):
    """
    write string to text file
    Args:
         filename: name of file
         text: text to write to file
    Return:
           Number of characters printed
    """

    with open(filename, "w", encoding="utf-8") as fl:
        text_count = fl.write(text)
    return text_count
