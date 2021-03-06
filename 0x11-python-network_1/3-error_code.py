#!/usr/bin/python3
# File: 3-error_code.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""
Sends a request to a URL and prints its response or error code.
usage: ./3-error_code.py http://0.0.0.0:5000/status_401
"""

import sys
from urllib import request, error

if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
        try:
            with request.urlopen(url) as response:
                print(response.read().decode('utf-8'))
        except error.HTTPError as ex:
            print('Error code: {}'.format(ex.code))
