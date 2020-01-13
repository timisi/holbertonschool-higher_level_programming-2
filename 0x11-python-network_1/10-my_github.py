#!/usr/bin/python3
"""Python script that takes in a string and sends a search request to the Star
Wars API
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    json_obj = r.json()
    id_num = json_obj.get('id')
    print(id_num)
