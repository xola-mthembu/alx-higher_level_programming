#!/usr/bin/python3
"""
This module lists all cities of a given state in the hbtn_0e_4_usa database,
protecting against SQL injection.
"""

import sys
import MySQLdb

def list_cities_by_state():
    """
    Lists all cities of a specified state from the database,
    sorted by the city ID.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query securely with user input
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """
    cursor.execute(query, (state_name,))

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()

    # Print the results in a comma-separated format
    if results:
        print(", ".join([city[0] for city in results]))
    else:
        print()

    # Close the cursor and the connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    list_cities_by_state()
