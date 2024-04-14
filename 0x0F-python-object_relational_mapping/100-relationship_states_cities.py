#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco” in the database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine
    engine = create_engine(f'mysql+mysqldb://{user}:{pw}@localhost/{dbase}')

    # Bind the engine to the metadata of the Base class
    Base.metadata.create_all(engine)

    # Create a Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create state and city
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)

    # Add to the session and commit
    session.add(new_state)
    session.commit()

    # Close the session
    session.close()
