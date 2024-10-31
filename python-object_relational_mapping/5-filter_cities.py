#!/usr/bin/python3
"""
This script lists all cities of a given state from the database hbtn_0e_4_usa.

Arguments:
    mysql_username: Your MySQL username.
    mysql_password: Your MySQL password.
    database_name: The name of the database to connect to.
    state_name: The name of the state to search for its cities.

The script connects to a MySQL server running on localhost at port 3306
and fetches all rows in the cities table for a given state,
sorted in ascending order by cities.id.
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

    # Prepare the SQL query to fetch cities based on the state name
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """
    # Execute the query with parameterized input to prevent SQL injection
    cursor.execute(query, (mysql_state_name,))

    # Fetch all results from the executed query
    cities = cursor.fetchall()

    # Print the cities in a comma-separated format
    print(", ".join([city[0] for city in cities]))

    # Close the cursor and database connection
    cursor.close()
    db.close()
