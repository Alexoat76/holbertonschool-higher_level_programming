#!/usr/bin/python3
# File: 11-delete_at.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Delete an item at a specific position in a list."""


def delete_at(my_list=[], idx=0):
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)
