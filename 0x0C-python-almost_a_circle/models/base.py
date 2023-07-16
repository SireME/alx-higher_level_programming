#!/usr/bin/python3
"""
base module with base class
"""


class Base:

    """
    base class initialisation
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ serialise list/dic to json str """
        ld = list_dictionaries
        if ld is None or len(ld) == 0:
            return "[]"
        import json
        return json.dumps(ld)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save json str to file """
        filename = cls.__name__ + ".json"
        objn = []
        if list_objs is not None:
            objn = [ins.to_dictionary() for ins in list_objs]
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(objn))

    @staticmethod
    def from_json_string(json_string):
        """deserialise json string """
        ld = json_string
        if ld is None or len(ld) == 0:
            return []
        import json
        return json.loads(ld)

    @classmethod
    def create(cls, **dictionary):
        """return instance with set attributes"""
        if cls.__name__ == "Rectangle":
            instance = cls(1, 55)
        else:
            instance = cls(77)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """ load and return instances from dictionary
        of attributes
        """
        try:
            filename = cls.__name__ + ".json"
            # read insatnce data from a json file containing list
            # of dictionary values
            with open(filename, "r") as f:
                filecont = f.read()
            fileldic = cls.from_json_string(filecont)
            # return list of instances using create static method
            return [cls.create(**ins) for ins in fileldic]
        except FileNotFoundError:
            return []
