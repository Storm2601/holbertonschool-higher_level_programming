#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa

Args:
    username (str): The username for the MySQL database
password (str): The password for the MySQL database
database (str): The name of the database

The script connects to a MySQL server running on localhost at port 3306
and fetches all rows in the cities table, sorted in ascending order by id
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;
    """
    cursor.execute(query)

    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()
