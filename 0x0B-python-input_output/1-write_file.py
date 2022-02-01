#!/usr/bin/python3
# File: 1-write_file.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""This Module defines a file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.
    Return: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
