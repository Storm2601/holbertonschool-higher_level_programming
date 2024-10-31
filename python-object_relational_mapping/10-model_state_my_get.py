#!/usr/bin/python3
"""
This script prints the State object with the name passed
as an argument from the database hbtn_0e_6_usa.

It takes four arguments:
    mysql_username: Your MySQL username.
    mysql_password: Your MySQL password.
    database_name: The name of the database to connect to.
    state_name: The name of the state to search for.

The script connects to a MySQL server running on localhost at port 3306,
fetches the State object that matches the given name from the `states` table,
and prints its id if found, or "Not found" if no match exists.
"""

# Import the sys module for command line arguments
import sys
# Import create_engine for DB connection
from sqlalchemy import create_engine
# Import sessionmaker for ORM sessions
from sqlalchemy.orm import sessionmaker
# Import Base and State from model_state
from model_state import Base, State

if __name__ == "__main__":
    # Retrieve command line arguments for MySQL connection and state name
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_database = sys.argv[3]
    mysql_state_name = sys.argv[4]

    # Create a SQLAlchemy engine to connect to the MySQL database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        mysql_username, mysql_password, mysql_database), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a session instance
    session = Session()

    # Query to retrieve the state that matches the given name
    states = session.query(State).filter(
        State.name == mysql_state_name).first()

    # Print the id of the state if found, otherwise print "Not found"
    if states:
        print(states.id)
    else:
        print("Not found")

    # Close the session to free resources
    session.close()
