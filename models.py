from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker,DeclarativeBase

class Base(DeclarativeBase):
    pass

class Officer(Base):
    __tablename__='officers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rank = Column(String)
    badge_no=Column(Integer)