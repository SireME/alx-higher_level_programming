#!/usr/bin/python3
"""
Write a function that returns the JSON representation of an object (string):

Prototype: def to_json_string(my_obj):
You don’t need to manage exceptions if the object can’t be serialized.
"""


def to_json_string(my_obj):
    """
    return json representation of an object

    Args:
         my_obj: string object to convert to json object
    Return:
           json object
    """
    import json
    return json.dumps(my_obj)
