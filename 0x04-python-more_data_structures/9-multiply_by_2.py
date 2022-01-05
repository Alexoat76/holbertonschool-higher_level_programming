#!/usr/bin/python3
# File: 9-multiply_by_2.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Return a new dictionary with all values multipled by 2."""


def multiply_by_2(a_dictionary):
    return ({k: a_dictionary[k] * 2 for k in a_dictionary})
