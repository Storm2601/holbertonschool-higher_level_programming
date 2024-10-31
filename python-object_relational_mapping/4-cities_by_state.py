#!/usr/bin/python3
"""
This script retrieves and displays all cities along with their
associated states from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL database
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=mysql_database
    )

    # Create cursor object
    cursor = db.cursor()

    # Create and execute query
    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )

    # Fetch and display results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close database connection
    cursor.close()
    db.close()
