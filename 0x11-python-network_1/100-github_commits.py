#!/usr/bin/python3
"""Python script that takes 2 arguments in order to list 10 commits
(from the most recent to oldest)
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[1],
                                                              sys.argv[2])
    r = requests.get(url)
    json_obj = r.json()
    for commit in json_obj:
        author_name = commit.get('commit').get('author').get('name')
        print("{}: {}".format(commit.get('sha'), author_name))
