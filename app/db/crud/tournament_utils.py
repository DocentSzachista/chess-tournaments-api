from tkinter.messagebox import NO
from fastapi import HTTPException, Response
from sqlalchemy.orm import Session 
from .. import models
from ... import schemas

def get_tournaments(db: Session, skip: int = 0 , limit: int = 100):
    return db.query(models.Tournament).offset(skip).limit(limit).all()

def get_tournament(db: Session, id : int):
    tournament  = db.query(models.Tournament).filter(models.Tournament.id == id).first()
    if tournament == None:
        raise HTTPException(status_code = 404, detail="Not found")
    return tournament

def update_tournament(db: Session, id: int,  user_id : int, tournament_updated: schemas.Tournament):
    
    query = db.query(models.Tournament).filter(models.Tournament.id == id)

    tournament = query.first()

    if tournament == None:
         raise HTTPException(status_code=404,
                            detail=f"Tournament with given id = {id} doesn't exists")
    if tournament.ownerId != user_id:
        raise HTTPException(status_code=403,
                            detail=f"Not authorized to perform that request")
    query.update(tournament_updated.dict(), synchronize_session=False)
    
    db.commit()
    
    return query.first()    

def delete_tournament(db: Session, id: int):
    tournament  = db.query(models.Tournament).filter(models.Tournament.id == id).first()
    if tournament == None:
        raise HTTPException(status_code = 404, detail="Not found")
    tournament.delete(synchronize_session=False)
    db.commit()
    return Response(status_code = 204 )

def create_tournament(db: Session, user: schemas.Tournament, current_user: int):
    db_tournament = models.Tournament(
        address = user.address,
        city = user.city,
        name = user.name,
        countryState = user.countryState,
        roundsNumber =  user.roundsNumber,
        system =  user.system,
        startDate = user.startDate ,
        endDate = user.endDate,
        ownerId = current_user )
    db.add(db_tournament)
    db.commit()
    db.refresh(db_tournament)
    return db_tournament
