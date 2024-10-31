#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa.

Arguments:
    mysql_username: Your MySQL username.
    mysql_password: Your MySQL password.
    database_name: The name of the database to connect to.

The script connects to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by cities.id.
Results are displayed as <state name>: (<city id>) <city name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(City, State).join(State).order_by(City.id).all()

    # Set to track unique cities
    printed_cities = set()

    for city, state in results:
        # Create a unique identifier for the city (name and state)
        city_identifier = (city.name, state.name)

        # Print only if the city hasn't been printed before
        if city_identifier not in printed_cities:
            printed_cities.add(city_identifier)
            print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
