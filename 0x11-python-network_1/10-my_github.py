#!/usr/bin/python3
# File: 10-my_github.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""
given username and pw as param, get your id from Github api
usage: ./10-my_github.py [github_username] [github_pw]
"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    print(response.json().get("id"))
