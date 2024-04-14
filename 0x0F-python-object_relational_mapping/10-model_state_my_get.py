#!/usr/bin/python3
"""
This script prints the State object with the name passed as argument
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

    # Query the State object with the given name
    state = session.query(State).filter_by(name=sys.argv[4]).first()

    # Print the result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
