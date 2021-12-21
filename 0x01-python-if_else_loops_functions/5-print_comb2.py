#!/usr/bin/python3
# File: 5-print_comb2.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Print all numbers from 0 to 99 separated by ',' followed by a space"""
print(", ".join("{0:0>2}".format(i) for i in range(100)))
