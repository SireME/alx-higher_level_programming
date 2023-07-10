#!/usr/bin/python3
"""
Integer validator
"""


class BaseGeometry:
    """
    Create area scafold and integer validator
    """
    def area(self):
        """
        create public intsnace method that raises an exception

        Args:
             None
        Return:
             None
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """
        validate integer
        Args:
             name: reference to integer
             value: integer value

        Return:
               None
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
