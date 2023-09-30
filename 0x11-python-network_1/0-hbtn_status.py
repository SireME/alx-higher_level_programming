#!/usr/bin/python3
"""
This script that gets the status of a website
"""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as request:
    response = request.read()
    print(f"Body response:")
    print(f"    - type: {type(response)}")
    print(f"    - content: {response}")
    print(f"    - utf8 content: {response.decode('utf-8')}")
