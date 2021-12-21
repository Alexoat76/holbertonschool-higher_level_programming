#!/usr/bin/python3
# File: 9-print_last_digit.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Print the last digit of a number and return it."""


def print_last_digit(number):
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
