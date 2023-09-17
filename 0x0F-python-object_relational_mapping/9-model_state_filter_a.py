#!/usr/bin/python3
"""
print all rows containing letter a in name
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv as av


if __name__ == "__main__":
    db = f"mysql+mysqldb://{av[1]}:{av[2]}@localhost/{av[3]}"
    engine = create_engine(db)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(State.id)
    result = result.filter(State.name.like('%a%')).all()
    for state in result:
        print(f'{state.id}: {state.name}')
    session.close()
