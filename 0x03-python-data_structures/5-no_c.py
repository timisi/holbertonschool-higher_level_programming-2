def no_c(my_string):
    new_string = my_string[:]
    len_newstr = len(new_string)
    i = 0
    while i < len_newstr:
        if new_string[i] == 'c' or new_string[i] == 'C':
            new_string = new_string[:i] + new_string[i + 1:]
            len_newstr = len_newstr - 1
        else:
            i = i + 1
    return new_string
