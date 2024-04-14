#!/usr/bin/python3
"""
This script lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    # Create the engine and session
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print all State objects containing 'a'
    for state in session.query(State) \
                        .filter(State.name.like('%a%')) \
                        .order_by(State.id):
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
