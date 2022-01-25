#!/usr/bin/python3
# File: 101-locked_class.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""
Defines class with no class or object attribute
Control dynamically created instance attributes
https://www.python-course.eu/python3_slots.php
"""


class LockedClass():
    """
    prevent user from creating new instance attribute dynamically
    unless attribute is "first_name"

    >>> a = LockedClass()
    >>> a.first_name = 'Alex'
    >>> a.first_name
    'Alex'

    >>> a.last_name = 'AoAt'
    Traceback (most recent call last):
    ...
    AttributeError: 'LockedClass' object has no attribute 'last_name'
    """

    __slots__ = "first_name"
