#!/usr/bin/python3
# File: 4-only_diff_elements.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Return a set of all elements present in only one set."""


def only_diff_elements(set_1, set_2):
    return (set_1 ^ set_2)
