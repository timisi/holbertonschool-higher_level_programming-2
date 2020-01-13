#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""


import urllib.request


req = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    the_page = response.read()
    content = the_page.decode('utf-8')
    print("Body response:")
    print("\t- type: {}".format(type(the_page)))
    print("\t- content: {}".format(the_page))
    print("\t- utf8 content: {}".format(content))
