#!/usr/bin/python3
# File: 4-list_division.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Divides two lists element by element.
 Returns:
        A new list of length list_length containing all the answers
        of divisions.
"""


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            answer = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            answer = 0
        except ZeroDivisionError:
            print("division by 0")
            answer = 0
        except IndexError:
            print("out of range")
            answer = 0
        finally:
            new_list.append(answer)
    return new_list
