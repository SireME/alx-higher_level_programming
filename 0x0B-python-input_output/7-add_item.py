#!/usr/bin/python3
"""
Write a script that adds all arguments to a Python list,
and then save them to a file:

You must use your function save_to_json_file
                             from 5-save_to_json_file.py
You must use your function load_from_json_file
                            from 6-load_from_json_file.py
The list must be saved as a JSON representation in a
                                  file named add_item.json
If the file doesn’t exist, it should be created
You don’t need to manage file permissions / exceptions.
"""
from sys import argv
import json
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_and_save_arguements_to_file():
    """
    add all arguments to python list and save as file

    Args:
         None
    Return:
          None
    """
    arguments = []
    if len(argv) == 1:
        arguments = []
    elif len(argv) > 1:
        arguments = argv[1:]

    # reading from json str from file
    try:
        json_load = load_from_json_file("add_item.json")
    except FileNotFoundError:
        json_load = []
        with open("add_item.json", "w") as fl:
            fl.write(json.dumps(json_load))

    # append arguments from read file json
    for i in arguments:
        json_load.append(i)

    # write appended content to file
    save_to_json_file(json_load, "add_item.json")


add_and_save_arguements_to_file()
