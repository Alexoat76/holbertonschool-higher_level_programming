#!/usr/bin/python3
# File: 101-remove_char_at.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Create a copy of the string without the character at position n."""


def remove_char_at(str, n):
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
