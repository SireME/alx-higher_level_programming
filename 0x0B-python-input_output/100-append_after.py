#!/usr/bin/python3
"""
function that inserts line of tectto a file atfer each line
containing a specific text
"""


def append_after(filename="", search_string="", new_string=""):
    """
    search for specific string in line and print another string
    at line ending if string present
    args:
         filenmae:name of file to read from
         search_string: string being searched
         new_string: new string to insert
    """
    with open(filename, 'r+') as file:
        # store all file content as list of strings
        lines = file.readlines()

        # move cursor to the start of file
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')
        file.truncate()
