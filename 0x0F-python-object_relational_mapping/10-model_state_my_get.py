#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # Create a new Engine instance.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create all tables in the engine.
    Base.metadata.create_all(engine)

    # Create a new Session instance.
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database and get the State object with the given name.
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Print the id of the state if found, else print Not found.
    if state:
        print(state.id)
    else:
        print("Not found")
