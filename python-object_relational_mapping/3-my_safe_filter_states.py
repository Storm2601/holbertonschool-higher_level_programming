#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states table
of the database hbtn_0e_0_usa where the name matches the argument.

Arguments:
    mysql_username: Your MySQL username.
    mysql_password: Your MySQL password.
    database_name: The name of the database to connect to.
    state_name: The name of the state to search for.

The script connects to a MySQL server running on localhost at port 3306
and fetches all rows in the states table with the name matching the argument,
sorted in ascending order by id. It uses parameterized queries to prevent
SQL injection.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Retrieve command-line arguments for MySQL credentials and state name
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_database = sys.argv[3]
    mysql_state_name = sys.argv[4]

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

    # Execute a query to select rows from states where name matches state_name
    query = "SELECT * FROM states WHERE name = %s " \
            "ORDER BY id ASC"
    cursor.execute(query, (mysql_state_name,))

    # Fetch all results from the executed query
    states = cursor.fetchall()

    # Print each state in the results
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()
