#!/usr/bin/python3
# File: 8-json_api.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""
given letter as param, POST to http://0.0.0.0:5000/search_user
usage: ./8-json_api.py [letter only]
"""

import sys
import requests


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    query = sys.argv[1] if len(sys.argv) > 1 else ""
    # if len(query) > 0 and not query[0].isalpha():
    #     query = ""
    form_data = [('q', query)]
    response = requests.post(url, data=form_data)
    try:
        json_content = response.json()
        if json_content:
            print('[{}] {}'.format(json_content['id'], json_content['name']))
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')
