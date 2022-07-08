from sqlalchemy.orm import Session 
from .. import models
from ... import schemas

def get_tournaments(db: Session, skip: int = 0 , limit: int = 100):
    return db.query(models.Tournament).offset(skip).limit(limit).all()

def create_tournament(db: Session, user: schemas.Tournament):
    db_tournament = models.Tournament(
        address = user.address,
        city = user.city,
        name = user.name,
        countryState = user.countryState,
        roundsNumber =  user.roundsNumber,
        system =  user.system,
        startDate = user.startDate ,
        endDate = user.endDate )
    db.add(db_tournament)
    db.commit()
    db.refresh(db_tournament)
    return db_tournament