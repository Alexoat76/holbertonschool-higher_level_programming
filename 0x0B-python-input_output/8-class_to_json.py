#!/usr/bin/python3
# File: 8-class_to_json.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""This Module defines a Python class-to-JSON function."""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object"""
    return obj.__dict__
