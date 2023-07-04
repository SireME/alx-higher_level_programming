#!/usr/bin/python3
"""
within: print a square with the charcter #
"""


def print_square(size):
    """print square using # character"""
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    square = ""
    for i in range(size):
        square += "#" * size + "\n"
    square = square[0:-1]
    print(square)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
