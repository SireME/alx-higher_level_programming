#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends
a request to the URL and displays the body of the respons
"""


if __name__ == '__main__':
    import requests
    from sys import argv
    rsp = requests.get(argv[1])
    status = rsp.status_code
    if status < 400:
        print(rsp.text)
    else:
        print(f"Error code: {status}")
