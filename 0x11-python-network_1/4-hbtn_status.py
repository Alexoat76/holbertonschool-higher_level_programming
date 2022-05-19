#!/usr/bin/python3
# File: 4-hbtn_status.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""
fetch https://intranet.hbtn.io/status; display response
Usage: ./4-hbtn_status.py | cat -e
"""
import requests


if __name__ == '__main__':
    response = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(response.text)))
    print('\t- content: {}'.format(response.text))
