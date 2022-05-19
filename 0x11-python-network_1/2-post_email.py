#!/usr/bin/python3
# File: 2-post_email.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""
given URL & email as params, send POST req to URL, display response body utf-8
usage: ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
"""

import sys
from urllib import request, parse


if __name__ == '__main__':
    if len(sys.argv) > 2:
        url = sys.argv[1]
        email = sys.argv[2]
        form_data = bytes(parse.urlencode([('email', email)]), 'utf-8')
        with request.urlopen(sys.argv[1], data=form_data) as response:
            print(response.read().decode('utf-8'))
