#!/usr/bin/python3
"""Contains the class definition of a State and an instance Base"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database.

    Attributes:
        id (str): The state's id.
        name (sqlalchemy.Integer): The state's name.
        cities (sqlalchemy.orm.relationship): The state's cities.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
