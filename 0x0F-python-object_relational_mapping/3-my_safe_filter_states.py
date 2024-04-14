#!/usr/bin/python3
"""
This module filters states by exact name match from the database hbtn_0e_0_usa,
safely, protecting from SQL injection.
"""

import sys
import MySQLdb


def safe_filter_states():
    """
    Connects to the database and filters states by user input.
    Implements safe query practices to prevent SQL injection.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_searched = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Secure way to format SQL queries with user input
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_searched,))

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()

    # Print the results
    for state in results:
        print(state)

    # Close the cursor and the connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    safe_filter_states()
