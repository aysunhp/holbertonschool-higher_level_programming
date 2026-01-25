#!/usr/bin/python3
"""
Defines a State class and Base instance
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base instance
Base = declarative_base()


class State(Base):
    """
    State class mapped to the states table
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
