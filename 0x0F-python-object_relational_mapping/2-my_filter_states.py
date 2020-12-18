#!/usr/bin/python3
"""script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument:
Take 4 arguments: mysql username, mysql password,
database name and state name searched"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor
    up = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC"\
        .format(argv[4])
    cursor.execute(up)
    list_ = cursor.fetchall()
    for row in list_:
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    db.close()
