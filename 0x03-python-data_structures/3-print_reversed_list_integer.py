#!/usr/bin/python3
# File: 3-print_reversed_list_integer.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Print all integers of a list in reverse order."""


def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
