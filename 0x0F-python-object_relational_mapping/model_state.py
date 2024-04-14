#!/usr/bin/python3
"""
Contains the class def of a State and instance Base = declarative_base().
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents a state for a MySQL database.
    __tablename__: the name of the MySQL table to store States.
    id: unique integer, can't be null and is a primary key.
    name: string of max 128 characters, can't be null.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
