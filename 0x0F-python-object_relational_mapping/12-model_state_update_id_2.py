#!/usr/bin/python3
""" Changes the name of a State object from the database hbtn_0e_6_usa """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # create connection to db
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, db_name))

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()

    # get the state with id=2 and update its name
    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"

    # commit the changes to the database
    session.commit()

    # close the session
    session.close()
