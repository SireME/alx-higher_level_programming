#!/usr/bin/python3
"""
Write a script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa
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

    # add new state to database
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    result = session.query(State)
    result = result.filter(State.name == "Louisiana").first()

    if result:
        print(result.id)
    else:
        print("Not found")
    session.close()
