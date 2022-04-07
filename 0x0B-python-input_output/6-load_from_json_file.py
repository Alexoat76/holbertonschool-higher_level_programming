#!/usr/bin/python3
# File: 6-load_from_json_file.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>
"""This Module defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
