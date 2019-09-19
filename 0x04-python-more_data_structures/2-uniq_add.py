#!/usr/bin/python3
def uniq_add(my_list=[]):
    numbs = list(set(my_list))
    res = 0
    for i in numbs:
        res += i
    return res
