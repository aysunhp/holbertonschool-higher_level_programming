#!/usr/bin/python3
"""
Print the State object with the name passed as argument
from the database hbtn_0e_6_usa (SQL injection safe)
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    search_name = sys.argv[4]

    # Create engine
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(username, password, db_name),
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query using filter to prevent SQL injection
    state = session.query(State).filter(State.name == search_name).first()

    # Print result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close session
    session.close()
