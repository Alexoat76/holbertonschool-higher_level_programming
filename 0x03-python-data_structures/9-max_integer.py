#!/usr/bin/python3
# File: 9-max_integer.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Find the biggest integer of a list."""


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    big = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > big:
            big = my_list[i]

    return (big)
