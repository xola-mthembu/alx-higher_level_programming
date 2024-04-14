#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
using SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Import Base and State class


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine with the 'mysql+mysqldb' dialect
    engine = create_engine(f'mysql+mysqldb://{un}:{pw}@localhost/{dbase}')

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query for all State objects, sorted by id
    states = session.query(State).order_by(State.id).all()

    # Print each state id and name
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
