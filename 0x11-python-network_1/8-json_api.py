#!/usr/bin/python3
"""
Write a Python script that takes in a letter
and sends a POST request to
http://0.0.0.0:5000/search_user with
the letter as a parameter.
"""


if __name__ == '__main__':
    import requests
    from sys import argv
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data={'q': q})
    try:
        mdict = r.json()
        id, name = mdict.get('id'), mdict.get('name')
        if len(mdict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(mdict.get('id'), mdict.get('name')))
    except Exception:
        print("Not a valid JSON")
