#!/usr/bin/python3
# File: 5-filter_cities.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""
This script return cities that are in the state given (tables 'cities' 'states)
parameters given to script: username, password, database, state
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
    sql_cmd = """SELECT cities.name
                 FROM states
                 INNER JOIN cities ON states.id = cities.state_id
                 WHERE states.name LIKE %s
                 ORDER BY cities.id ASC"""
    cursor.execute(sql_cmd, (argv[4], ))

    # Printing all cities of a given state in a database separated by commas
    print(', '.join(["{:s}".format(row[0]) for row in cursor.fetchall()]))

    cursor.close()
    db.close()
