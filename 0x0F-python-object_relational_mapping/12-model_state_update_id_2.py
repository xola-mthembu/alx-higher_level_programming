#!/usr/bin/python3
"""
This script changes the name of a State object from the database hbtn_0e_6_usa.
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

    # Update the State object with id 2
    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()

    # Close the session
    session.close()
