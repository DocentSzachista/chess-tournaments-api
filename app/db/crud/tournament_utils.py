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

def update_tournament(db: Session, id: int,  user_id : int, tournament_updated: schemas.TournamentDB):
    
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

def create_tournament(db: Session, new_tournament: schemas.TournamentDB, current_user: int):
    db_tournament = models.Tournament( 
        address = new_tournament.address,
        city = new_tournament.city,
        name = new_tournament.name,
        countryState = new_tournament.countryState,
        roundsNumber =  new_tournament.roundsNumber,
        system =  new_tournament.system,
        tempo = new_tournament.tempo,
        startDate = new_tournament.startDate ,
        endDate = new_tournament.endDate,
        ownerId = current_user )
    db.add(db_tournament)
    db.commit()
    db.refresh(db_tournament)
    return db_tournament
