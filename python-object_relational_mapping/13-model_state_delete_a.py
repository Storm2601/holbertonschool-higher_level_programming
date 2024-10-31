#!/usr/bin/python3
"""
This script deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.

It takes three arguments:
    mysql_username: Your MySQL username.
    mysql_password: Your MySQL password.
    database_name: The name of the database to connect to.

The script connects to a MySQL server running on localhost at port 3306,
fetches all State objects that match the given criteria, and deletes them
from the database.
"""

# Import the sys module for command line arguments
import sys
# Import create_engine for database connection
from sqlalchemy import create_engine
# Import sessionmaker for ORM sessions
from sqlalchemy.orm import sessionmaker
# Import Base and State from model_state
from model_state import Base, State

if __name__ == "__main__":
    # Retrieve command line arguments for MySQL connection
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_database = sys.argv[3]

    # Create a SQLAlchemy engine to connect to the MySQL database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        mysql_username, mysql_password, mysql_database), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a session instance
    session = Session()

    # Query to retrieve all states that contain the letter 'a' in their name
    delete = session.query(State).filter(State.name.like('%a%')).all()

    # Loop through the states and delete each one
    for row in delete:
        session.delete(row)

    # Commit the changes to the database
    session.commit()
    # Close the session to free resources
    session.close()
