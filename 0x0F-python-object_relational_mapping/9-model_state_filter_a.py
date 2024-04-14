#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
that contain the letter 'a' in their name, sorted by their IDs.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Set up the database engine
    engine_url = f'mysql+mysqldb://{user}:{pw}@localhost/{dbase}'
    engine = create_engine(engine_url)

    # Create a Session class bound to the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State objects containing 'a', sorted by id
    states = session.query(State).filter(State.name.like('%a%')) \
                                 .order_by(State.id).all()

    # Print each state found
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the database session
    session.close()
