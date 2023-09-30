#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends
a request to the URL and displays the body of
the response (decoded in utf-8).
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        url_to_fetch = sys.argv[1]
        with request.urlopen(url_to_fetch) as response:
            page_contents = response.read().decode('UTF-8')
            print(page_contents)
    except error.HTTPError as http_error:
        print('Error code:', http_error.code)
