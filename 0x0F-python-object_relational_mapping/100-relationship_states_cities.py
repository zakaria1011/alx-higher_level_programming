#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco”
 from the database hbtn_0e_100_usa.
 """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":
    from sys import argv

    username, password, dbname = argv[1], argv[2], argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}'
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California", cities=[City(name="San Francisco")])

    session.add(california)

    session.commit()

    session.close()
