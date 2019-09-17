#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    else:
        for x in matrix:
            for y in x[:-1]:
                print("{:d} ".format(y), end="")
            print("{:d}".format(x[-1]))
