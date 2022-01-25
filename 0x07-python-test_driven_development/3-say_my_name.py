#!/usr/bin/python3
# File: 3-say_my_name.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""
This is the "Say My Name" module.
The Say My Name module takes one required parameter and one optional.
It prints "My name is (first) (last)" where (first) and (last) are the args.
"""


def say_my_name(first_name, last_name=""):
    """Print My name is (first) (last) if given, else print error.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
