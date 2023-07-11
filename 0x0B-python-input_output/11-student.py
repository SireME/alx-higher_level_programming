#!/usr/bin/python3
"""
 Write a class Student that defines a student by:
                 (based on 10-student.py)
 Public instance attributes:
 first_name
 last_name
 age
 Instantiation with first_name, last_name and age:
 def __init__(self, first_name, last_name, age):
 Public method def to_json(self, attrs=None): that retrieves
  a dictionary representation of a Student instance
 (same as 8-class_to_json.py):
 If attrs is a list of strings, only attributes name
 contain in this list must be retrieved.
 Otherwise, all attributes must be retrieved
 Public method def reload_from_json(self, json):
 that replaces all attributes of the Student instance:
 You can assume json will always be a dictionary
 A dictionary key will be the public attribute name
 A dictionary value will be the value of the public attribute
"""


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        return dictionary representation of class
        Args:
             None
        Return:
               dictionary of attributes and their corresponding values
               if attribute not a string, print entire attributes
        """
        if isinstance(attrs, list):
            for i in attrs:
                if not isinstance(i, str):
                    return self.__dict__
        else:
            return self.__dict__
        dictn = {}
        for att in attrs:
            for key, value in self.__dict__.items():
                if key == att:
                    dictn[key] = value
                    break
        return dictn

    def reload_from_json(self, json):
        """
        replace all attributes of instance
        Args:
             json: dictionary containing new attributes
        Return:
               None
        """
        self.__dict__ = json
