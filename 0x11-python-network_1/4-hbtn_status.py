#!/usr/bin/python3
"""
Script that fetches the content of the URL https://intranet.hbtn.io/status
with response package
"""
import requests


if __name__ == '__main__':
    url_to_fetch = "https://intranet.hbtn.io/status"
    response = requests.get(url_to_fetch)
    response_text = response.text
    print("Body response:")
    print("\t- type: {}".format(type(response_text)))
    print("\t- content: {}".format(response_text))
