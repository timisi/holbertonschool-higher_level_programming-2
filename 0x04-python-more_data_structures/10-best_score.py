#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        key_name = (sorted(a_dictionary.items(), key=lambda x : x[1], reverse = True))[0][0]
        return key_name
