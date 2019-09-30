#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as errex:
        print("Exception: {}".format(errex), file=sys.stderr)
        return None
