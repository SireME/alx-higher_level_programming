#!/usr/bin/python3
"""
square module with rectangle inheritance
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class that inherites from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overide str method with Square parameters"""
        s = self.width
        return f"[Square] ({self.id}) {self.x}/{self.y} - {s}"

    @property
    def size(self):
        """ get the size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.heigth = value

    def to_dictionary(self):
        """dictionary representation of rectangle"""
        dic_rep = {}
        dic_rep["id"], dic_rep["size"] = self.id, self.width
        dic_rep["x"], dic_rep["y"] = self.x, self.y
        return dic_rep

    def update(self, *args, **kwargs):
        """update instance attributes using position and keyword"""
        if args and len(args) >= 1:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) == 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
