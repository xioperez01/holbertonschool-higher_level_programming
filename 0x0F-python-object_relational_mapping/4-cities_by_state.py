#!/usr/bin/python3
"""
return info from both tables (tables 'cities' 'states)
parameters given to script: username, password, database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    """Connect to a MySQL server."""

    cursor = db.cursor()
    cmd = """SELECT cities.id, cities.name, states.name
                 FROM states
                 INNER JOIN cities ON states.id = cities.state_id
                 ORDER BY cities.id ASC"""
    cursor.execute(cmd)

    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
