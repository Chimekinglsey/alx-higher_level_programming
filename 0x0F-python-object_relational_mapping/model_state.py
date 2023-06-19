#!/usr/bin/python3
"""
Using sqlalchemy to implement MySQLdb server connection
"""
from sqlalchemy.ext.declaratives import declarative_base
from sqlalchemy import Integer, String, MetaData, Column

metadata = MetaData()
Base = declarative_base(metadata)


class State(Base):
    """This state class inherits from Base class that allows us to dynamically
    the connection object and use it to create a table"""
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=True)
