#!/usr/bin/python3
"""
Using sqlalchemy to implement MySQLdb server connection
"""
import sqlalchemy
from sqlalchemy.ext.declaratives import declarative_base
from sqlalchemy import Integer, String, create_engine, Column

engine = create_engine('mysql://chime:chime@localhost:3306/mysqlalchemy')
connection = engine.connect()
Base = declarative_base()


class State(Base):
    """This state class inherits from Base class that allows us to dynamically
    create table using Base.metadata.create_all(engine).
    engine uses URL to create mysql server framework with define prams
    then connection calls connect() on the engine that establishes the
    connection to our database
    then Base.metadata will take all the activities done in the engine throught
    the connection object and use it to create a table"""
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=True)


Base.metadata.create_all(engine)
