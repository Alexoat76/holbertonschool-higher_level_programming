#!/usr/bin/python3
# File: 0-read_file.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""This Module defines a text file-reading function."""


def read_file(filename=""):
    """Read and print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
