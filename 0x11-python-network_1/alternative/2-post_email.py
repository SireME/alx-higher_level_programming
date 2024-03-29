#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an
email, sends a POST request to the passed URL with
the email as a parameter, and displays the body of
the response (decoded in utf-8)
"""

import urllib.request
import sys
import urllib.parse
if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("utf-8")
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(url) as request:
        req = request.read()
        print(req.decode("utf-8"))
