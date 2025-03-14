from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker,DeclarativeBase

class Base(DeclarativeBase):
    pass

class Officer(Base):
    __tablename__='officers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rank = Column(String)

    badge = relationship("Badge", back_populates="officer", uselist=False)
    motorbike = relationship("Motorbike", back_populates="assigned_officer", uselist=False)

class Badge(Base):
    __tablename__ = 'badges'
    id = Column(Integer, primary_key=True)
    badge_number = Column(String, unique=True)
    officer_id = Column(Integer, ForeignKey('officers.id'), unique=True) 

    officer = relationship('Officer', back_populates='badge')

class Case(Base):
    __tablename__ = 'cases'
    id = Column(Integer, primary_key=True)
    case_no = Column(String, unique=True)
    details = Column(String)
    

class Suspect(Base):
    __tablename__ = 'suspects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)

class Motorbike(Base):
    __tablename__ = 'motorbikes'
    id = Column(Integer, primary_key=True)
    registration_number = Column(String, unique=True)
    model = Column(String)
    status = Column(String, default='Available')
    officer_id = Column(Integer, ForeignKey('officers.id'))


    assigned_officer = relationship("Officer", back_populates="motorbike")