#!/usr/bin/python3
"""
create db class
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv as av


if __name__ == "__main__":
    db = f"mysql+mysqldb://{av[1]}:{av[2]}@127.0.0.1:3306/{av[3]}"
    engine = create_engine(db)

    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(State.id).all()
    for instance in result:
        print(f'{instance.id}: {instance.name}')
    session.close()
