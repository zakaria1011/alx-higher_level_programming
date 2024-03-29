#!/usr/bin/python3
"""Script that prints all City objects from the database hbtn_0e_14_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database))

    Base.metadata.create_all(engine)

    session = Session(engine)
    query = session.query(State, City).join(City).order_by(City.id)
    result = query.all()

    for state, city in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
