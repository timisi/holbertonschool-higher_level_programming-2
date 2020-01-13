#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)."""


import urllib.request
import urllib.parse
import sys


url = sys.argv[1]

req = urllib.request.Request(url)
try:
    with urllib.request.urlopen(req) as response:
        page_info = response.read().decode('utf-8')
        print(page_info)
except urllib.error.URLError as e:
    print("Error code: {}".format(e.code))
