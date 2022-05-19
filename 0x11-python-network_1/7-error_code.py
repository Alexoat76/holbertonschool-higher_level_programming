#!/usr/bin/python3
# File: 7-error_code.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""
Sends a request to a URL and prints its response or error code
usage: ./7-error_code.py http://0.0.0.0:5000/status_401
"""

import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
        response = requests.get(url)
        if response.status_code >= 400:
            print('Error code: {}'.format(response.status_code))
        else:
            print(response.text)
