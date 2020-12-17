#!/usr/bin/python3
"""
Script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa:
take 3 arguments: mysql username, mysql password and database name
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    up = "SELECT * FROM states WHERE name LIKE '%N' ORDER BY states.id ASC"
    cursor.execute(up)
    for row in cursor.fetchall():
        if row[1][0] == 'N':
            print(row)
    cursor.close()
    db.close()
