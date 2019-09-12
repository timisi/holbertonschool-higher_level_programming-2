#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    lis = dir(hidden_4)
    for names in lis:
        if names[0:2] != "__":
            print(names)
