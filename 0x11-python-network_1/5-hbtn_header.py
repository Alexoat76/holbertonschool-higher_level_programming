#!/usr/bin/python3
# File: 5-hbtn_header.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""
given URL as parameter, fetch URL and display value from reponse header
usage: ./5-hbtn_header https://intranet.hbtn.io
"""

import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
        response = requests.get(url)
        if 'X-Request-Id' in response.headers:
            print(response.headers['X-Request-Id'])
