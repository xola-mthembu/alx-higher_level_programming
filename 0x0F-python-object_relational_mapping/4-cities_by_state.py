#!/usr/bin/python3
"""
This module lists all cities from the hbtn_0e_4_usa database,
including the name of the state each city belongs to.
"""

import sys
import MySQLdb


def list_cities():
    """
    Lists all cities from the database along with the state name,
    sorted by the city ID.
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
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;
    """
    cursor.execute(query)

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()

    # Print the results
    for city in results:
        print(city)

    # Close the cursor and the connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities()
