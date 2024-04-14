#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa.
If no state is present, prints 'Nothing'.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Import Base and State class


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine
    engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@localhost/{dbase}')

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the first State object by id
    first_state = session.query(State).order_by(State.id).first()

    # Check if any state was found
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()
