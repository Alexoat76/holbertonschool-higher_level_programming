#!/usr/bin/python3
# File: 101-add_attribute.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""A module for manipulating objects."""


def add_attribute(obj, name, value):
    """Add a new attribute to an object if possible.
    Args:
        obj (any): The object to modify.
        name (str): The name of the attribute.
        value (any): The value of the attribute.
    """
    if ('__dict__' in dir(obj)) and (type(obj.__dict__) is dict):
        obj.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")
