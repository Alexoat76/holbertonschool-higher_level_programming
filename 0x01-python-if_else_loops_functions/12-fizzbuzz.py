#!/usr/bin/python3
# File: 12-fizzbuzz.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""Print the numbers from 1 to 100 separated by a space.
   For multiples of three, print Fizz instead of the number.
   For multiples of five, print Buzz instead of the number.
   For multiples of three and five, print FizzBuzz instead of the number.
    """


def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
