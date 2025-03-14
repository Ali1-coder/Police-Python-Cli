from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker,DeclarativeBase

class Base(DeclarativeBase):
    pass

