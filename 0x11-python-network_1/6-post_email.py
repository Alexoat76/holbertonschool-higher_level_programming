#!/usr/bin/python3
# File: 6-post_email.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""
given URL & email as params, send POST req to URL, display response body utf-8
usage: ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
"""

import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) > 2:
        url = sys.argv[1]
        email = sys.argv[2]
        form_data = [('email', email)]
        response = requests.post(url, data=form_data)
        print(response.text)
