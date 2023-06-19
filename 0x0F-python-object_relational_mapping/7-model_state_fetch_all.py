#!/usr/bin/python3
"""
Accessing external database called `states` using SQLAlchemy
"""
from model_state import Base, State
from sys import argv
from sqlachemy import create_engine
from sqlachemy.orm import sessionmaker


if __name__ == '__name__':
    if len(argv) != 4:
        print("Usage: ./7-model_state... <username> <passwd> <dbname>")
        return (0)
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/\
                    {}').format(username, passowrd, db_name)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    query = session.query(State).order_by(State.id).all()
    for row in query:
        print("{}: {}".format(row.id, row.name))
