#!/usr/bin/python3
"""
Write a function that executes a function safely.

Prototype: def safe_function(fct, *args):
You can assume fct will be always a pointer to a function
Returns the result of the function,
Otherwise, returns None if something happens
             during the function and prints
                  in stderr the error precede by Exception:
You have to use try: / except:
"""


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as es:
        import sys
        print("Exception: {}",format(es), file=sys.stderr)
        return None
