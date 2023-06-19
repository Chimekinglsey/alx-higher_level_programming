#!/usr/bin/python3
import sqlalchemy
from sqlalchemy.ext.declaratives import declarative_base
from sqlalchemy import Integer, String, create_engine, Column

engine = create_engine('mysql://chime:chime@localhost:3306/mysqlalchemy')
connection = engine.connect()
Base = declarative_base()
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True, nullable=False,\
    primary_key=True)
    name = Column(String(128), nullable=True)
Base.metadata.create_all(engine)
