from operator import index
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, column
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key = True, index = True)
    firstname = Column(String, nullable = False)
    lastname = Column(String, nullable = False)
    email = Column(String, unique = True, index = True, nullable=False)
    gender = Column(String, nullable = False, index = True)
    birthYear = Column(String, nullable = False)
    rankPZszach = Column(Integer, nullable = False)
    password = Column(String, nullable = False)
    ranking = relationship("FIDERanking", uselist=False, back_populates="user")

    tournaments = relationship("Tournament")
    participants = relationship("Participant")
    # ranking = relationship("FIDERanking", back_populates="user", uselist=False)

class FIDERanking(Base):
    __tablename__ = "FIDERanking"
    
    id = Column(Integer, primary_key = True, index = True)
    blitz =  Column(Integer, nullable=False)
    rapid =  Column(Integer, nullable=False)
    standard =  Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    
    user = relationship("User", back_populates="ranking")


class Tournament(Base):
    __tablename__ = "tournaments"

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

    ownerId = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    rounds = relationship("Round")
    participants = relationship("Participant")

class Round(Base):
    __tablename__="rounds"
    
    id = Column(Integer, primary_key = True, index = True)
    tournamentId = Column(Integer, ForeignKey('tournaments.id', ondelete="CASCADE"), nullable=False)
    roundNumber = Column(Integer)

class Participant(Base):
    __tablename__="participants"

    id = Column(Integer, primary_key = True, index = True)
    participantId = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    tournamentID  = Column(Integer, ForeignKey('tournaments.id', ondelete="CASCADE"), nullable=False)
    points = Column(Integer)
