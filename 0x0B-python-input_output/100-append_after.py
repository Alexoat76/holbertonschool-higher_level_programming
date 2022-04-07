#!/usr/bin/python3
# File: 100-append_after.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""This Module defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file."""
    with open(filename, 'r', encoding='utf-8') as f:
        line_list = []
        while True:
            line = f.readline()
            if line == "":
                break
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(line_list)
