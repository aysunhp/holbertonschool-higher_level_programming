#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # create engine
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query all states ordered by id
    states = session.query(State).order_by(State.id).all()

    # display results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
