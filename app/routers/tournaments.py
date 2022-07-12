from fastapi import APIRouter, Depends, Path, Response
from ..schemas import TournamentState, CountryState, TournamentTempo, Tournament
# from ..db import database
from sqlalchemy.orm import Session 
from ..db.crud import tournament_utils

from ..dependencies import get_db
from ..oauth2 import get_current_user

router = APIRouter(
    prefix="/tournaments",
    tags=["Tournaments"],
    responses={404: {"description": "Not found"}}
)


@router.get("/{tournament_id}")
def retrieve_tournament(tournament_id: int = Path(title="Id of the tournament we want to get", ge=0),
db: Session = Depends(get_db) ):

    return tournament_utils.get_tournament(db, tournament_id)

@router.get("/")
def retrieve_tournaments(
    name : str | None = None, 
    tempo: TournamentTempo | None = None,
    city : str | None = None,
    countryState: CountryState | None = None,
    tournamentState : TournamentState | None = None,
    db: Session = Depends(get_db) 
  ):
  return tournament_utils.get_tournaments(db)
#   return fake_db

@router.post(path="/")
def add_tournament(tournament : Tournament, db: Session = Depends(get_db), user_id: int = Depends(get_current_user))->Tournament:
    
    new_tournament = tournament_utils.create_tournament(db, tournament, user_id )

    return new_tournament

@router.put(path="/{tournament_id}")
def update_tournament(
  tournament : Tournament,
  tournament_id : int = Path(title="Id of the tournament we want to get", ge=0),
  user_id: int = Depends(get_current_user),
  db: Session = Depends(get_db) 
   ):
  
  return tournament_utils.update_tournament(db, tournament_id, user_id, tournament ) 

@router.delete(path="/{tournament_id}")
def delete_tournament(
  tournament_id : int = Path(title="Id of the tournament we want to get", ge=0),
  user_id: int = Depends(get_current_user) ,
  db: Session=Depends(get_db)):

  return tournament_utils.delete_tournament(db, tournament_id)