#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQL
from sys import argv

if __name__ = "__main__":

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = cursor.db()
    cmd = """SELECT cities.id, cities.name, states.name
                 FROM states
                 INNER JOIN cities ON states.id = cities.state_id
                 ORDER BY cities.id ASC"""
    cursor.execute(cmd)
    list_ = cursor.fetchall()
    for row in list_:
        print(row)
    cursor.close()
    db.close()
