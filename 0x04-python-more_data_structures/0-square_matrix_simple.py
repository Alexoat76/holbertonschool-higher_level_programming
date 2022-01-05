#!/usr/bin/python3
# File: 0-square_matrix_simple.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Compute the square value of all integers of a matrix."""


def square_matrix_simple(matrix=[]):
    return ([list(map(lambda x: x * x, row)) for row in matrix])
