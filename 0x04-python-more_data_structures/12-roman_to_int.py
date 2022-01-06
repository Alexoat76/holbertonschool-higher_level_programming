#!/usr/bin/python3
# File: 12-roman_to_int.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Converts a roman numeral to an integer."""


def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return (0)

    roman_dxnry = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    num = 0

    for i in range(len(roman_string)):
        if roman_dxnry.get(roman_string[i], 0) == 0:
            return (0)

        if (i != (len(roman_string) - 1) and
                roman_dxnry[roman_string[i]] <
                roman_dxnry[roman_string[i + 1]]):
            num += roman_dxnry[roman_string[i]] * -1

        else:
            num += roman_dxnry[roman_string[i]]
    return (num)
