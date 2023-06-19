#!/usr/bin/python3
"""
Accessing external database called `states` using SQLAlchemy
"""
from model_state import Base, State
from sys import argv, exit
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: ./7-model_state... <username> <passwd> <dbname>")
        exit(1)
    '''
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    '''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format\
    (sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id)
    for row in query:
        print("{}: {}".format(row.id, row.name))
