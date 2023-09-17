#!/usr/bin/python3
"""
Write a script that changes the name of a
State object from the database hbtn_0e_6_usa
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
    result = result.filter(State.id == 2).first()

    # change name where id is 2
    result.name = "New Mexico"
    session.commit()
    session.close()
