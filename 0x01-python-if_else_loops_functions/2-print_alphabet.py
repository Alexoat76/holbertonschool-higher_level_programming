#!/usr/bin/python3
# File: 2-print_alphabet.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Print the alphabet in lowercase, not followed by a new line."""
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
