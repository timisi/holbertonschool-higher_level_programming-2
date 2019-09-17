#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    else:
        for x in matrix:
            for y in x[:-1]:
                print("{} ".format(y), end="")
            print("{}".format(x[-1]))
