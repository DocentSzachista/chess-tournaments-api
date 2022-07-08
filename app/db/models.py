from operator import index
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, column
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key = True, index = True)
    firstname = Column(String, nullable = False)
    lastname = Column(String, nullable = False)
    email = Column(String, unique = True, index = True)
    gender = Column(Enum, nullable = False, index = True)
    birthYear = Column(String)
    rankPZszach = Column(Integer)
    # fideRankingId = Column(Integer, ForeignKey('ranking.id'))
    password = Column(String, nullable = False)
    # ranking = relationship("FIDERanking", back_populates="user", uselist=False)

class FIDERanking(Base):
    __tablename__ = "FIDERanking"
    
    id = Column(Integer, primary_key = True, index = True)
    blitz =  Column(Integer)
    rapid =  Column(Integer)
    standard =  Column(Integer)

    # user = relationship("User", back_populates="ranking")


class Tournament(Base):
    __tablename__ = "Tournaments"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    city = Column(String)
    address = Column(String)
    tempo = Column(String)
    countryState = Column(String)
    roundsNumber = Column(Integer)
    system = Column(String)
    startDate = Column(String)
    endDate = Column(String)
