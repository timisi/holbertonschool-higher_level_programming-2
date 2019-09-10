#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        n = number % 10
    elif number == 0:
        n = 0
    elif number < 0:
        n = abs(number) % 10
    print("{}".format(n), end="")
    return n
