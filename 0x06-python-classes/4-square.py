#!/usr/bin/python3
# File: 4-square.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""
This is the "Square" module.
This module provides a simple Square class with initialize size.
Defaults size to 0. Raise error on invalid size inputs.
Methods Getter and Setter properties for size.
Method area returns size of area of the square.
"""


class Square:
    """A class that defines a square by size and can compute area"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size
