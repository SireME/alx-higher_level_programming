#!/usr/bin/python3
"""
create db class
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv as av


Base = declarative_base()
db = f"mysql+mysqldb://{av[1]}:{av[2]}@127.0.0.1:3306/{av[3]}"
engine = create_engine(db)


class State(Base):
    """
    state class that maps to table
    """
    __tablename__ = "state"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
