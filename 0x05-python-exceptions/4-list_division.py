#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = 0
    new_list = []
    for n in range(list_length):
        try:
            result = my_list_1[n] / my_list_2[n]
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except TypeError:
            result = 0
            print("wrong type")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
