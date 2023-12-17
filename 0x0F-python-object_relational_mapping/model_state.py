#!/usr/bin/python3
"""Definition of a State and an instance Base = declarative_base()"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    Defination of a State Class with attributes
        id (uuid): a column of an auto-generated, unique integer,
                  not null and is a primary key.
        name (str): a column of a string with maximum 128 characters
                    and not null.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
