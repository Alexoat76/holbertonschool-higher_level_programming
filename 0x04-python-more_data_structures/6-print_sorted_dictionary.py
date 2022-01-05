#!/usr/bin/python3
# File: 6-print_sorted_dictionary.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Print a dictionary by ordered keys."""


def print_sorted_dictionary(a_dictionary):
    [print("{}: {}".format(k, a_dictionary[k])) for k in sorted(a_dictionary)]
