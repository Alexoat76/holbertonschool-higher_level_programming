#!/usr/bin/python3
# File: 4-print_square.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""
This is the "Print Square" module.
The Print Square module prints a square using "#".
The argument supplied should determine the width/height of square.
"""


def print_square(size):
    """Print a square with the # character.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
