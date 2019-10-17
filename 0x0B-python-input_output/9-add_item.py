#!/usr/bin/python3
"""Module ´´9-add_item´´ adds all arguments to a Python list, and then save
them the add_item.json file"""


import json
import sys
import os

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
new_list = []

if os.path.exists(filename):
    new_list = load_from_json_file(filename)

for argum in sys.argv[1:]:
    new_list.append(argum)

save_to_json_file(new_list, filename)
