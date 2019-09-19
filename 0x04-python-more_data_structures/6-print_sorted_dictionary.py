#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    names = sorted(a_dictionary)
    for n in names:
        print("{}: {}".format(n, a_dictionary[n]))
