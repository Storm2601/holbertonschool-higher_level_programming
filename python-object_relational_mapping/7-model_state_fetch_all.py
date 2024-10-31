#!/usr/bin/python3

"""
This script lists all State objects from the database hbtn_0e_6_usa.

Arguments:
    mysql_username: Your MySQL username.
    mysql_password: Your MySQL password.
    database_name: The name of the database to connect to.

The script connects to a MySQL server running on localhost at port 3306
and fetches all rows in the states table, sorted in ascending order by id.
"""

# Importing the sys module to handle command-line arguments.
import sys
# Importing create_engine to create the database engine.
from sqlalchemy import create_engine
# Importing sessionmaker to create session objects.
from sqlalchemy.orm import sessionmaker
# Importing Base and State from the model_state module.
from model_state import Base, State

if __name__ == "__main__":
    # Retrieve command-line arguments for MySQL credentials and database name.
    mysql_username = sys.argv[1]  # MySQL username.
    mysql_password = sys.argv[2]  # MySQL password.
    mysql_database = sys.argv[3]   # Database name.

    # Create a database engine using the provided credentials
    # and database name.
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            mysql_username, mysql_password, mysql_database
        ),
        pool_pre_ping=True
    )

    # Create a new session to interact with the database.
    Session = sessionmaker(bind=engine)  # Bind the session to the engine.
    session = Session()  # Create a session instance.

    # Query the State table and order results by id in ascending order.
    states = session.query(State).order_by(State.id).all()

    # Iterate through the results and print the id and name of each state.
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()  # Close the session to free up resources.
