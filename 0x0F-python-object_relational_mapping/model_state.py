#!/usr/bin/python3
"""
We are progressing to use ORM declarative_base for Syncing
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata)


class State(Base):
    """
    This inherits from our Base class. Creates table using MetaData()
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
