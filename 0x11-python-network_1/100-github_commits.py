#!/usr/bin/python3
"""
This script collects the first 10 commits from a
specific repo with its author
"""
from requests import get
from sys import argv

url = f"https://api.github.com/repos/{argv[1]}/{argv[2]}/commits"
r = get(url).json()

for i in range(10):
    result = ""
    result += r[i]["sha"]
    result += ": "
    result += r[i]["commit"]["author"]["name"]
    print(result)
