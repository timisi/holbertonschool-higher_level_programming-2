#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        ky_n = (sorted(a_dictionary.items(), key=lambda x: x[1], reverse=True))
        return ky_n[0][0]
