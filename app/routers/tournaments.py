
from fastapi import APIRouter, Path, Response
from ..models import TournamentState, CountryState, TournamentTempo, Tournament
from ..db import database
router = APIRouter(
    prefix="/tournaments",
    tags=["Tournaments"],
    responses={404: {"description": "Not found"}}
)

fake_db  = database.read_db("tournaments")


@router.get("/{tournament_id}")
def retrieve_tournament(tournament_id: int = Path(title="Id of the tournament we want to get", ge=0)):
    if len(fake_db) > tournament_id:
        return fake_db[tournament_id]
    else: 
        return Response(status_code=404)

@router.get("/")
def retrieve_tournaments(
    name : str | None = None, 
    tempo: TournamentTempo | None = None,
    city : str | None = None,
    countryState: CountryState | None = None,
    tournamentState : TournamentState | None = None 
  ):
  return fake_db

@router.post(path="/")
def add_tournament(tournament : Tournament)->Tournament:
    fake_db.append(tournament.__dict__)
    return tournament

@router.put(path="/{tournament_id}")
def update_tournament(tournament_id : int = Path(title="Id of the tournament we want to get", ge=0)):
  return {"message":"Nothing here yet"} 

@router.delete(path="/{tournament_id}")
def delete_tournament(tournament_id : int = Path(title="Id of the tournament we want to get", ge=0)):
  return {"message":"Nothing here yet"}