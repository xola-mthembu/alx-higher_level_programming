#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Check the command line arguments
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> <database_name> \
<state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    # Create a cursor object
    cursor = db.cursor()
    # Execute the SQL query with parameter
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))

    # Fetch and display the results
    for row in cursor.fetchall():
        print(row)

    # Close the cursor and the connection
    cursor.close()
    db.close()
