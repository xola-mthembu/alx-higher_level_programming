#!/usr/bin/python3
"""
A script that lists all states with names starting with 'N' from the database `hbtn_0e_0_usa`.
The script takes three arguments: the MySQL username, password, and database name.
"""

import MySQLdb
import sys

def filter_states(username, password, dbname):
    """
    Connects to the MySQL database and prints all states starting with 'N' in ascending order by states.id.
    """
    try:
        db = MySQLdb.connect(host="127.0.0.1", port=3306, user=username,
                             passwd=password, db=dbname)
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print("Error connecting to MySQL: ", e)
        return

if __name__ == "__main__":
    if len(sys.argv) == 4:
        filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
