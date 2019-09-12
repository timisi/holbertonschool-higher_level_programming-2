#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ar_num = len(sys.argv) - 1
    if ar_num == 0:
        print("{} arguments.".format(ar_num))
    elif ar_num == 1:
        print("{} argument:".format(ar_num))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(ar_num))
        n = 1
        for ar_str in sys.argv[1:]:
            print("{}: {}".format(n, ar_str))
            n = n + 1
