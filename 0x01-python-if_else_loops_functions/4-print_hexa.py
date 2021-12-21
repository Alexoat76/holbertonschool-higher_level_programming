#!/usr/bin/python3
# File: 4-print_hexa.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Print all numbers from 0 to 98 in decimal and in hexadecimal"""
for number in range(0, 99):
    print("{} = {}".format(number, hex(number)))
