#!/usr/bin/python3
"""
Write a function that prints an integer.

Prototype: def safe_print_integer_err(value):
value can be any type (integer, string, etc.)
The integer should be printed followed by a new line
Returns True if value has been correctly
          printed (it means the value is an integer)
Otherwise, returns False and prints
              in stderr the error precede by Exception:
You have to use try: / except:
You have to use "{:d}".format() to print as integer
You are not allowed to use type()
"""


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as es:
        import sys
        print("Exception: {}".format(es), file=sys.stderr)
        return False
