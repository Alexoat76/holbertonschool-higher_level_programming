#!/usr/bin/python3
# File: 0-safe_print_list.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Print x elements of a list.
Returns:
        The number of elements printed.
"""


def safe_print_list(my_list=[], x=0):
    index = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            index += 1
        except IndexError:
            break
    print()
    return index
