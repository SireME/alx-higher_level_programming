#!/usr/bin/python3
"""
print first row from db
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
    result = session.query(State).order_by(State.id).first()
    if result is None:
        print"Nothing"()
    else:
        print(f'{result.id}: {result.name}')
    session.close()
