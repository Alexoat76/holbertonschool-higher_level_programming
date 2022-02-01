#!/usr/bin/python3
# File: 3-to_json_string.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""This Module defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    return json.dumps(my_obj)
