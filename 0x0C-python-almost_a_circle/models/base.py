#!/usr/bin/python3
"""
base module with base class
"""
import csv
import json
import turtle


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save json str to csv file """
        filename = cls.__name__ + ".csv"
        objn = []
        if list_objs is not None:
            objn = [ins.to_dictionary() for ins in list_objs]
            newobjn = []
            rec = ["id", "width", "height", "x", "y"]
            sq = ["id", "size", "x", "y"]
            for dictxn in objn:
                tempdic = {}
                if filename == "Rectangle.csv":
                    for key, value in dictxn.items():
                        for j in rec:
                            if key == j:
                                tempdic[key] = value
                                break
                elif filename == "Square.csv":
                    for key, value in dictxn.items():
                        for j in sq:
                            if key == j:
                                tempdic[key] = value
                                break
                newobjn.append(tempdic)

        with open(filename, "w", encoding="utf-8") as f:
            header = 0
            if newobjn:
                for data in newobjn:
                    writer = csv.DictWriter(f, fieldnames=data.keys())
                    if header == 0:
                        writer.writeheader()
                    writer.writerow(data)
                    header = 1
            else:
                f.write("")

    @classmethod
    def load_from_file_csv(cls):
        """ load and return instances from csv file
        """
        try:
            filename = cls.__name__ + ".csv"
            # read insatnce data from a json file containing list
            # of dictionary values
            list_dic = []
            with open(filename, "r") as f:
                reader = csv.DictReader(f)
                for dictxn in reader:
                    for key, value in dictxn.items():
                        dictxn[key] = int(value)
                    list_dic.append(dictxn)
            # return list of instances using create static method
            return [cls.create(**ins) for ins in list_dic]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ draw all instances rectangle and square"""
        window = turtle.Screen()
        turtle.speed(1)
        # Draw rectangles
        for rectangle in list_rectangles:
            turtle.color("blue", "green")
            turtle.begin_fill()
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)
            turtle.left(90)
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)
            turtle.left(90)
            turtle.end_fill()
        # Draw squares
        for square in list_squares:
            turtle.color("blue", "pink")
            turtle.begin_fill()
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for j in range(4):
                turtle.forward(square.size)
                turtle.left(90)
            turtle.end_fill()
        turtle.done()
