#!/usr/bin/python3
# File: 0-lookup.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Defines an object attribute lookup function."""


def lookup(obj):
    """Returns a list of available attributes and methods of an object"""
    return (dir(obj))
