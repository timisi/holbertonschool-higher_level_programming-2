def element_at(my_list, idx):
    rang_li = len(my_list)
    if idx > (rang_li - 1):
        return
    elif idx < 0:
        return
    else:
        return my_list[idx]
