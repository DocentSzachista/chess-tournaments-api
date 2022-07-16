from fastapi import HTTPException, Response
from sqlalchemy.orm import Session
from .. import models
from ... import schemas

def get_tournaments(db: Session, params: dict , skip: int = 0 , limit: int = 100):
    
    query = db.query(models.Tournament)
    for attr in [x for x in params if params[x] is not None]:
        search = f"%{params[attr]}%" 
        query = query.filter(getattr(models.Tournament, attr).like(search) )
    return query.offset(skip).limit(limit).all()

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

def add_user_to_tournament(db: Session, tournament_id: int, user_id: int):
    
    already_signed_up = db.query(models.Participant.id).filter_by(
        tournamentID = tournament_id, participantId = user_id  ).first() is not None
    if already_signed_up:
        raise HTTPException(status_code= 409, detail="Already signed up" )
    is_owner =  db.query(models.Tournament.ownerId).filter_by(ownerId = user_id).first() is not None
    if is_owner:
        raise HTTPException(status_code= 403, detail="You cant sign up for your own tournament" )
    db_participant = models.Participant(
        tournamentID = tournament_id,
        participantId = user_id
        )
    db.add(db_participant)
    db.commit()

    query = db.query(
        models.Participant.points, 
        models.User.firstname,
        models.User.lastname
    ).filter(
        models.User.id == user_id,
        models.Participant.tournamentID == tournament_id
    ).first()
    return query

def retrieve_participants(db: Session, tournament_id: int):
    query = db.query(
        models.Participant.points, 
        models.User.firstname,
        models.User.lastname
    ).filter(
        models.User.id == models.Participant.participantId,
        models.Participant.tournamentID == tournament_id    
    ).all()
    return query 

# TODO: see why its throwing an error 
def sign_out_participant(db: Session, tournament_id: int, user_id: int): 
    participant  = db.query(models.Participant).filter(
        models.Participant.tournamentID == tournament_id,
        models.Participant.participantId == user_id, ).first()
    if participant == None:
        raise HTTPException(status_code = 404, detail="Not found")
    participant.delete(synchronize_session=False)
    db.commit()
    return Response(status_code = 204 )