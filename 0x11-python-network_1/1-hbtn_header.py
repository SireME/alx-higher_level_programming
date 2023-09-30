#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""

import urllib.request
from sys import argv

url = argv[1]

with urllib.request.urlopen(url) as request:
    response = request.headers
    print(response["X-Request-Id"])
