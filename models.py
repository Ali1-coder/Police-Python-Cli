from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker,DeclarativeBase

class Base(DeclarativeBase):
    pass

class Officer(Base):
    __tablename__='officers'

    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rank = Column(String)

    # One officer can have one badge, one motorbike, and can handle many cases.
    badge = relationship("Badge", back_populates="officer", uselist=False)
    motorbike = relationship("Motorbike", back_populates="assigned_officer", uselist=False)
    cases=relationship('Case',back_populates='officer')

class Badge(Base):
    __tablename__ = 'badges'
    id = Column(Integer, primary_key=True)
    badge_number = Column(String, unique=True)
    officer_id = Column(Integer, ForeignKey('officers.id'), unique=True) 
    
    # A badge belongs to one officer.
    officer = relationship('Officer', back_populates='badge')

case_suspects = Table(
    'case_suspects', Base.metadata,
    Column('case_id', Integer, ForeignKey('cases.id'), primary_key=True),
    Column('suspect_id', Integer, ForeignKey('suspects.id'), primary_key=True)
)


class Case(Base):
    __tablename__ = 'cases'
    id = Column(Integer, primary_key=True)
    case_no = Column(String, unique=True)
    details = Column(String)
    officer_id = Column(Integer, ForeignKey('officers.id'))
    
    # A case is handled by one officer and can have many suspects.
    officer = relationship("Officer", back_populates="cases")
    suspects = relationship("Suspect", secondary=case_suspects, back_populates="cases")
    

class Suspect(Base):
    __tablename__ = 'suspects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    
    # A suspect can be involved in many cases.
    cases = relationship("Case", secondary=case_suspects, back_populates="suspects")

class Motorbike(Base):
    __tablename__ = 'motorbikes'
    id = Column(Integer, primary_key=True)
    registration_number = Column(String, unique=True)
    model = Column(String)
    status = Column(String, default='Available')
    officer_id = Column(Integer, ForeignKey('officers.id'))

    # A motorbike is assigned to one officer.
    assigned_officer = relationship("Officer", back_populates="motorbike")

