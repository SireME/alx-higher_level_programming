#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends
a request to the URL and displays the body of
the response (decoded in utf-8).
"""

import sys
from urllib import request, error


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as req:
            print(req.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
