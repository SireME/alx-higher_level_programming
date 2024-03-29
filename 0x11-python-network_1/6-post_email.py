#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email
address, sends a POST request to the passed URL
with the email as a parameter, and finally
displays the body of the response.
"""


if __name__ == '__main__':
    import requests
    from sys import argv
    payload = {'email': argv[2]}
    rsp = requests.post(argv[1], data=payload)
    print(rsp.text)
