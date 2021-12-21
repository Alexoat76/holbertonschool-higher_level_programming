#!/usr/bin/python3
# File: 3-print_alphabet.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Print the alphabet in lowercase, except 'q' and 'e'"""
for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")
