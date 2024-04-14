#!/usr/bin/python3
"""
This module filters states from the database hbtn_0e_0_usa that start with 'N'.
"""

import sys
import MySQLdb


def filter_states():
    """
    Connects to the database and filters states starting with 'N'.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()

    # Print the results
    for state in results:
        print(state)

    # Close the cursor and the connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states()
