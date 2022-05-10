#!/usr/bin/python3
# File: 4-cities_by_state.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""
This script return info from both tables (tables 'cities' 'states)
parameters given to script: username, password, database
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

    # Create cursor to exec queries using SQL; join two tables for all info
    cursor = db.cursor()
    sql_cmd = """SELECT cities.id, cities.name, states.name
                 FROM states
                 INNER JOIN cities ON states.id = cities.state_id
                 ORDER BY cities.id ASC"""
    cursor.execute(sql_cmd)

    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
