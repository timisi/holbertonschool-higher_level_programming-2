#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tuple_a = 0, 0
    elif len(tuple_a) == 1:
        aux_tuple = tuple_a[0], 0
        tuple_a = aux_tuple
    if len(tuple_b) == 0:
        tuple_b = 0, 0
    elif len(tuple_b) == 1:
        aux_tuple = tuple_b[0], 0
        tuple_b = aux_tuple
    res1 = tuple_a[0] + tuple_b[0]
    res2 = tuple_a[1] + tuple_b[1]
    new_tuple = res1, res2,
    return (new_tuple)
