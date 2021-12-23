#!/usr/bin/python3
# File: 3-infinite_add.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Print the addition of all arguments."""

if __name__ == "__main__":
    import sys

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
