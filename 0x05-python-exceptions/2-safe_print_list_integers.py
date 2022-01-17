#!/usr/bin/python3
# File: 2-safe_print_list_integers.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Print the first x elements of a list that are integers.
Returns:
        The number of elements printed.
"""


def safe_print_list_integers(my_list=[], x=0):
    index = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            index += 1
        except (ValueError, TypeError):
            continue
    print()
    return index
