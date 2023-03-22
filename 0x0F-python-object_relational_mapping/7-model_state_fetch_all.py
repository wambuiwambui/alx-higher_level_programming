#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # check for correct usage
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # create the connection to the db
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # create a Session instance
    session = Session()

    # get all State objects from the database and sort by id
    states = session.query(State).order_by(State.id).all()

    # print each state in the desired format
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # close the session
    session.close()
