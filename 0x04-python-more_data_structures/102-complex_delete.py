#!/usr/bin/python3
# File: 102-complex_delete.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Delete keys with a specific value in a dictionary."""


def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        for k, v in a_dictionary.items():
            if v == value:
                del a_dictionary[k]
                break

    return (a_dictionary)
