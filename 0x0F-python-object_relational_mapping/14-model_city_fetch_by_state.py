#!/usr/bin/python3
"""lists all Cities objects from the database hbtn_0e_14_usa"""
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for query in (session.query(State.name, City.id, City.name)
                     .filter(State.id == City.state_id)):
        print(query[0] + ": (" + str(query[1]) + ") " + query[2])
