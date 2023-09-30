#!/usr/bin/python3
"""
Write a Python script that takes your GitHub
credentials (username and password) and uses
the GitHub API to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/users/{}'.format(argv[1])
    rq = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    print(rq.json().get('id'))
