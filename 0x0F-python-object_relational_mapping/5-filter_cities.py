#!/usr/bin/python3
"""Module that that lists all cities from the database"""


import MySQLdb
import sys


if __name__ == "__main__":

    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=MY_USER,
        passwd=MY_PASS,
        db=MY_DB
    )
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                 LEFT JOIN states\
                 ON states.id = cities.state_id\
                 WHERE states.name = (%s) ORDER BY cities.id ASC",
                (state_name,))
    table = cur.fetchall()

    str_cities = ""
    for row in table[:-1]:
        str_cities = str_cities + row[0] + ", "
    str_cities = str_cities + table[-1][0]

    print(str_cities)
    cur.close()
    db.close()
