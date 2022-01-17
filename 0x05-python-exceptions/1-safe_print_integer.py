#!/usr/bin/python3
# File: 1-safe_print_integer.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Print an integer with "{:d}".format()."
Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
