#!/usr/bin/python3
"""
Write a function that prints a text with 2 new
             lines after each of these characters: ., ? and :

Prototype: def text_indentation(text):
text must be a string, otherwise raise a
   TypeError exception with the message text must be a string
There should be no space at the beginning or
                            at the end of each printed line
You are not allowed to import any module
"""


def text_indentation(text):
    """ print lines after specific characters"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = [".", "?", ":"]
    splitable = ""
    for nc in text:
        if nc in characters:
            splitable += nc
            splitable += "😀"
        else:
            splitable += nc

    lines = splitable.split("😀")
    incre = 0
    for line in lines:
        line = line.strip()
        print(line, end="")
        if incre != len(lines) - 1:
            print("\n\n", end="")
        incre += 1


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
