#!/usr/bin/python3
"""
Script that fetches the content of URL
with response package
"""


if __name__ == '__main__':
    import requests

    url_to_fetch = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url_to_fetch)
    response_text = response.text
    print("Body response:")
    print("\t- type: {}".format(type(response_text)))
    print("\t- content: {}".format(response_text))
