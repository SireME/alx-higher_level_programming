#!/usr/bin/python3
"""
Write a class MyList that inherits from list:

Public instance method: def print_sorted(self): that
              prints the list, but sorted (ascending sort)
You can assume that all the elements of the list will be of type int
You are not allowed to import any module
"""


class MyList(list):
    """class that extends the built-in list
    class with additional functionality.
    """

    def print_sorted(self):
        """Sorts the list in ascending order and prints the sorted list.

        Args:
            None

        Returns:
            None

        Example:
            my_list = MyList([3, 1, 4, 2, 5])
            my_list.print_sorted()
            # Output: [1, 2, 3, 4, 5]
        """
        mlist = self.copy()
        mlist.sort()
        print(mlist)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
