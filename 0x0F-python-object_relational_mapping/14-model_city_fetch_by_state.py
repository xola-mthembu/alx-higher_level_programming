#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
sorted by city ids and grouped by state.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine
    engine = create_engine(f'mysql+mysqldb://{user}:{pw}@localhost/{dbase}')

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities joined with states, ordered by city ID
    cities = session.query(City).options(joinedload(City.state))\
                                .order_by(City.id).all()

    # Print each city's details, formatted as required
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
