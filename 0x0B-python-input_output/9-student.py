#!/usr/bin/python3
# File: 9-student.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>
"""This Module defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the Student."""
        return self.__dict__
