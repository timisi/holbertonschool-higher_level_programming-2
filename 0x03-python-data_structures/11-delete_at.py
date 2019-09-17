#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not my_list:
        return []
    else:
        if idx > len(my_list) - 1 or idx < 0:
            return my_list
        else:
            del my_list[idx]
            return my_list
