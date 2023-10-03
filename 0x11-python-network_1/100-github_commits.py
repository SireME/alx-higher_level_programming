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
    try:
        for i in range(10):
            rs = ""
            rs += r[i].get("sha")
            rs += ": "
            rs += r[i].get("commit").get("author").get("name")
            print(rs)
    except Exception:
        pass
