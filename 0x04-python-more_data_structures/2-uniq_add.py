#!/usr/bin/python3
# File: 2-uniq_add.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Add all unique integers in a list (once for each integer)."""


def uniq_add(my_list=[]):
    result = 0
    for x in set(my_list):
        result += x
    return (result)
