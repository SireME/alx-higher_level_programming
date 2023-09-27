#!/usr/bin/python3
"""
this file contains code to create db
table class
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship as rl

Base = declarative_base()


class State(Base):
    """
    state class that maps to
    sqlalchemy table
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = rl("City", back_populates="state", cascade="all, delete")
