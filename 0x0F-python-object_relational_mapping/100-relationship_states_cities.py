#!/usr/bin/python3
# File:  100-relationship_states_cities.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""
This script create state "California" with city attribute "San Francisco"
parameters given: username, password, database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()

    session.close()
