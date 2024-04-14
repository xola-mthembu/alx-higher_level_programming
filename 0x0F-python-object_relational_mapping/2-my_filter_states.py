#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )
    cursor = db.cursor()
    cursor.execute("SLCT * FROM states WHERE name = %s ORDER BY id ASC", (argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
