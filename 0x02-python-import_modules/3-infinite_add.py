#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ar_num = len(sys.argv) - 1
    if ar_num == 0:
        print("{}".format(ar_num))
    else:
        res = 0
        for ar_str in sys.argv[1:]:
            res = res + int(ar_str)
        print(res)
