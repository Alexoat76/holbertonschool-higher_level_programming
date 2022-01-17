#!/usr/bin/python3
# File: 3-safe_print_division.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Returns the division of a by b."""


def safe_print_division(a, b):
    try:
        x = a / b
    except ZeroDivisionError:
        x = None
    finally:
        print("Inside result: {}".format(x))
        return x
