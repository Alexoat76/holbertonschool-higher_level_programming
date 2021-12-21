#!/usr/bin/python3
# File: 7-islower.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Check for lowercase characters."""


def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
