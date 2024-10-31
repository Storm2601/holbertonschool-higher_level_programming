#!/usr/bin/python3

"""
This script lists all states from the database `hbtn_0e_0_usa`.

Arguments:
    mysql_username: MySQL username.
    mysql_password: MySQL password.
    database_name: Database name to connect to.

The script connects to a MySQL server running on localhost at port 3306
and retrieves all rows in the states table, ordered by id in ascending order.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Retrieve command-line arguments for MySQL credentials and database name
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_database = sys.argv[3]

    # Establish a connection to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=mysql_database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute a query to select all rows from the states table ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results from the executed query
    states = cursor.fetchall()

    # Print each state in the results
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()
