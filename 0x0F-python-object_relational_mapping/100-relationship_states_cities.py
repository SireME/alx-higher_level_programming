#!/usr/bin/python3
"""
print id of a particular state
"""
from relationship_city import Base, City
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv as av


if __name__ == "__main__":
    db = f"mysql+mysqldb://{av[1]}:{av[2]}@localhost/{av[3]}"
    engine = create_engine(db)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state1 = State(name="California")
    city1 = City(name="San Francisco", state_id=1)
    session.add(state1)
    session.add(city1)
    session.commit()
    session.close()
