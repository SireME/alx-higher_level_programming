#!/usr/bin/python3
"""
Write a script that deletes all State objects
with a name containing the letter a from
the database hbtn_0e_6_usa
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
    result = session.query(State)
    result = result.filter(State.name.like('%a%')).all()
    for state in result:
        # deleting each row at a time
        session.delete(state)
    session.commit()
    session.close()
