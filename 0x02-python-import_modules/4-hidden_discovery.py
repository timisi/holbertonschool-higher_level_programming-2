#!/usr/bin/python3
import hidden_4
lis = dir(hidden_4)
for names in lis:
    if names[0:2] != "__":
        print(names)
