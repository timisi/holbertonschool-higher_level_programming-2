#!/usr/bin/python3
"""Python script that takes 2 arguments in order to list 10 commits
(from the most recent to oldest)
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[2],
                                                              sys.argv[1])
    r = requests.get(url)
    json_obj = r.json()
    for num in range(0, 10):
        commit = json_obj[num]
        author_name = commit.get('commit').get('author').get('name')
        print("{}: {}".format(commit.get('sha'), author_name))
