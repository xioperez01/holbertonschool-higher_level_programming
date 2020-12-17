#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa:
Take 3 arguments: mysql username, mysql password and database name
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

	db = MySQLdb.connect(user=argv[1],
			     password=argv[2],
			     db=argv[3],
			     port=336,
			     host="localhost")

	cursor = db.cursor()
	cursor.execute("SELECT * FROM states ORDER BY id ASC")
	for row in cursor.fetchall():
		print(row)
	cursor.close()
	db.close()
