#!/usr/bin/python3
"""
This script adds the State object "Louisiana" to the database hbtn_0e_6_usa.

Arguments:
    mysql_username: Your MySQL username.
    mysql_password: Your MySQL password.
    database_name: The name of the database to connect to.

The script connects to a MySQL server running on localhost at port 3306
and adds a new state to the `states` table, printing its id after insertion.
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
    # Retrieve command line arguments for MySQL connection
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create a SQLAlchemy engine to connect to the MySQL database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a session instance
    session = Session()

    # Create a new State object for Louisiana
    new_state = State(name="Louisiana")
    # Add the new state to the session
    session.add(new_state)
    # Commit the session to save the new state to the database
    session.commit()

    # Print the id of the newly added state
    print(new_state.id)

    # Close the session to free resources
    session.close()
