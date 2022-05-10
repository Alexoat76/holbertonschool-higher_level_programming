#!/usr/bin/python3
# File: 10-model_state_my_get.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""
This script return state id given state name; SQL injection free
parameters given: username, password, database, state name to match
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
     Base.metadata.create_all(eng)
     Session = sessionmaker(bind=eng)
     session = Session()
     state = session.query(State).filter_by(name=argv[4]).first()
     if state is not None:
         print(str(state.id))
     else:
         print("Not found")

    session.close()
