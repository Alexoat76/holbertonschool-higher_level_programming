#!/usr/bin/python3
# File: 10-best_score.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Returns a key with the biggest integer value."""


def best_score(a_dictionary):
    if a_dictionary:
        return(max(a_dictionary, key=a_dictionary.get))
