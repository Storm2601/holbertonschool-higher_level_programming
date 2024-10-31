#!/usr/bin/python3
"""
This module defines the State class that represents the states table
in the database. It utilizes SQLAlchemy ORM for database interaction.

Attributes:
    id (int): The primary key for the state, automatically incremented.
    name (str): The name of the state, cannot be null.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """State class representing a state entry in the database."""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
