#!/usr/bin/python3

import sys

if __name__ == "__main__":
    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(count, '' if count == 1 else 's'))
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))
