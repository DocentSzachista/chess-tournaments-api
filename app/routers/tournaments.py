from xmlrpc.client import Boolean
from fastapi import APIRouter, Depends, Path, Response
from requests import delete
from ..schemas import TournamentState, CountryState, TournamentTempo, TournamentBase, TournamentDB, TournamentOut
from ..schemas import user
from sqlalchemy.orm import Session 
from ..db.crud import tournament_utils

from ..dependencies import get_db
from ..oauth2 import get_current_user

router = APIRouter(
    prefix="/tournaments",
    tags=["Tournaments"],
    responses={404: {"description": "Not found"}}
)

@router.get("/{tournament_id}", response_model=TournamentOut)
def retrieve_tournament(tournament_id: int = Path(title="Id of the tournament we want to get", ge=0),
db: Session = Depends(get_db) ):

    return tournament_utils.get_tournament(db, tournament_id)

@router.get("/", response_model=list[TournamentOut])
def retrieve_tournaments(
    name : str | None = None, 
    tempo: TournamentTempo | None = None,
    city : str | None = None,
    countryState: CountryState | None = None,
    tournamentState : TournamentState | None = None,
    db: Session = Depends(get_db) 
  ):
  params = locals().copy()
  params.pop("db") 
  return tournament_utils.get_tournaments(db, params)


@router.post(path="/")
def add_tournament(
  tournament : TournamentDB, 
  db: Session = Depends(get_db), 
  user_id: int = Depends(get_current_user))->TournamentDB:
 
    new_tournament = tournament_utils.create_tournament(db, tournament, user_id )
    return new_tournament

@router.put(path="/{tournament_id}")
def update_tournament(
  tournament : TournamentDB,
  tournament_id : int = Path(title="Id of the tournament we want to get", ge=0),
  user_id: int = Depends(get_current_user),
  db: Session = Depends(get_db)):
  
  return tournament_utils.update_tournament(db, tournament_id, user_id, tournament ) 

@router.delete(path="/{tournament_id}")
def delete_tournament(
  tournament_id : int = Path(title="Id of the tournament we want to get", ge=0),
  user_id: int = Depends(get_current_user) ,
  db: Session=Depends(get_db)):

  return tournament_utils.delete_tournament(db, tournament_id)

@router.get(path="/{tournament_id}/participants")
def retrieve_participants(
  tournament_id : int = Path(title="Id of the tournament we want to get", ge=0), 
  sort_by_score : Boolean = False,
  db: Session = Depends(get_db)):

  return tournament_utils.retrieve_participants(db, tournament_id)

@router.post(path="/{tournament_id}/signUp", #response_model=user.ParticipantOut
 )
def signup_for_tournament(
  tournament_id:  int = Path(title="Id of the tournament we want to get", ge=0),
  user_id: int = Depends(get_current_user),
  db: Session = Depends(get_db)):
  
  return tournament_utils.add_user_to_tournament(db, tournament_id, user_id)

@router.delete(path="/{tournament_id}/signOut")
def sign_out_from_tournament(
  tournament_id:  int = Path(title="Id of the tournament we want to get", ge=0), 
  user_id: int = Depends(get_current_user),
  db: Session = Depends(get_db)):
  
  return tournament_utils.sign_out_participant(db, tournament_id, user_id)

@router.post(path="/{tournament_id}/rounds")
def generate_new_round(
  tournament_id: int =Path(title="Id of the tournament we want to get", ge=0), 
  user_id: int = Depends(get_current_user),
  db: Session = Depends(get_db)   ):
  
  return tournament_utils.generate_round(db, tournament_id, user_id)
  