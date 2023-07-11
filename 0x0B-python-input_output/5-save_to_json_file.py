#!/usr/bin/python3
"""
Write a function that writes an Object to a
text file, using a JSON representation:

Prototype: def save_to_json_file(my_obj, filename):
You must use the with statement
You don’t need to manage exceptions if the object can’t be serialized.
You don’t need to manage file permission exceptions.
"""


def save_to_json_file(my_obj, filename):
    """
    write object to text file using json representation
    Args:
         my_obj: object to write
         filename: file to write representation to
    Return:
           nothing
    """

    with open(filename, "w", encoding="utf-8") as fl:
        import json
        fl.write(json.dumps(my_obj))
