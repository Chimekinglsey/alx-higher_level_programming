#!/usr/bin/python3
"""
Accessing external database called `states` using SQLAlchemy
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_count = session.query(State).filter(State.name == (argv[4],))
    try:
        print(state_count[0].id)
    except IndexError:
        print("Not found")
