#!/usr/bin/python3
"""
Write a Python file similar to model_state.py named
model_city.py that contains the class definition of a City.
"""
from model_city import City
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv as av

if __name__ == "__main__":

    db = f"mysql+mysqldb://{av[1]}:{av[2]}@localhost/{av[3]}"
    engine = create_engine(db)

    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)
    result = session.query(State, City)
    result = result.filter(City.state_id == State.id).all()
    for row in result:
        print(f"{row[0].name}: ({row[1].id}) {row[1].name}")
    session.close()
