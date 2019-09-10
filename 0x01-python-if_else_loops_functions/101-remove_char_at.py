#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        cpy_str = str[:n] + str[n + 1:]
        return (cpy_str)
    else:
        return (str)
