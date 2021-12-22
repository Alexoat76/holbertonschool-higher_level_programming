#!/usr/bin/python3
# File: 100-print_tebahpla.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Print the alphabet in reverse order alternating upper- and lower-case."""


for i in range(122, 96, -1):
    if i % 2 != 0:
        print("{:c}".format(i - 32), end="")
    else:
        print("{:c}".format(i), end="")
