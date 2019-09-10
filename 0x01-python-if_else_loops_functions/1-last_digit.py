#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
op_str = "Last digit of {} is {} and is greater than 5"
op_str0 = "Last digit of {} is {} and is 0"
op_str3 = "Last digit of {} is {} and is less than 6 and not 0"
if number > 5:
    print(op_str.format(number, number % 10))
elif number == 0:
    print(op_str0.format(number, number % 10))
elif number < 6 and number > 0:
    print(op_str3.format(number, number % 10))
elif number < 0:
    print(op_str3.format(number, (abs(number) % 10) * -1))
