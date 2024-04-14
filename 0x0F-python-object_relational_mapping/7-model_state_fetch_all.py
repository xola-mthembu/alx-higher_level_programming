#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Import Base and State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine
    engine = create_engine(f'mysql+mysqldb://{usr}:{psword}@localhost/{dbase}')
    Base.metadata.create_all(engine)

    # Create a Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for all State objects, sorted by id
    states = session.query(State).order_by(State.id).all()

    # Print each state id and name
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
