#!/usr/bin/python3
"""Definition of a City and an instance Base = declarative_base()"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    Defination of a City Class with attributes
        id (uuid): a column of an auto-generated, unique integer,
                  not null and is a primary key.
        name (str): a column of a string with maximum 128 characters
                    and not null.
        state_id (uuid): is a foregin key for state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
