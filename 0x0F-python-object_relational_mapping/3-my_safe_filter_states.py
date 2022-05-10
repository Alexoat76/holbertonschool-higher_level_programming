#!/usr/bin/python3
# File: 3-my_safe_filter_states.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""
This script return matching states
parameters given to script: username, password, database, state to match
                            and is safe from MySQL injections
NOTE: See 'http://bobby-tables.com/python'
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # Connect to database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # Create cursor to exec queries using SQL; match arg given
    cursor = db.cursor()
    sql_cmd = """SELECT *
                 FROM states
                 WHERE name=%s ORDER BY id ASC"""
    cursor.execute(sql_cmd, (argv[4],))

    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
