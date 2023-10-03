#!/usr/bin/python3
"""
This script collects the first 10 commits from a
specific repo with its author
"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    r = get(url).json()

    for i in range(10):
        result = ""
        result += r[i].get("sha")
        result += ": "
        result += r[i].get("commit").get("author").get("name")
        print(result)
