#!/usr/bin/python3
# File: 3-is_kind_of_class.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""
This module defines a class and inherited class-checking function.
"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
    """
    if isinstance(obj, a_class):
        return True
    return False
