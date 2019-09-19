#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replace_f = lambda x : replace if x == search else x
    new_list = list(map(replace_f, my_list))
    return new_list
