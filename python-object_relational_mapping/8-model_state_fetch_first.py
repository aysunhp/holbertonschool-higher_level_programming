#!/usr/bin/python3
"""
Print the first State object from the database hbtn_0e_6_usa
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

    # query first state ordered by id
    first_state = session.query(State).order_by(State.id).first()

    # display result
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # close session
    session.close()
