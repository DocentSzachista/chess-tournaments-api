from enum import Enum

from fastapi import FastAPI, Path, Response
from pydantic import BaseModel, Field
from .routers import tournaments
app = FastAPI(title="Chess tournaments API")

app.include_router(tournaments.router)

app.get("/")
def root():
    return {"message": "I am a teapot"}

# class TournamentTempo(str, Enum):
#     empty = ""
#     blitz = "blitz"
#     rapid = "rapid"
#     classic = "classic"

# class CountryState(str, Enum):
#     empty = ""
#     DS = "DS"
#     LB = "LB"
#     WM = "WM"

# class TournamentState(str, Enum):
#     planned = "planned"
#     ongoing = "ongoing"
#     finished = "finished"

# class Tournament(BaseModel): 
    
#     name: str = Field(
#         title = "The title of tournament", 
#         description = "Remember to not exceed its max lenght", 
#         max_length = 150,
#         example = "chess international 2022 in Wroclaw"
#         ) 
    
#     city: str = Field(
#         title = "City of the tournament", 
#         max_length = 50,
#         example = "Wrocław" 
#         )
    
#     address: str = Field(
#         title = "Address of a building where tournament takes place",
#         max_length=255,
#         example = "Krajowa 8"
#     )
    
#     tempo: TournamentTempo = Field(
#         default=None, 
#         title="tournament tempo", 
#         description="You must provide one of given types",
#         example = TournamentTempo.classic
#         )

#     countryState: CountryState = Field( 
#         default = None, 
#         title = "contains info about in which country state tournament takes part",
#         example = CountryState.DS 
#         )
    
#     startDate: str = Field(
#         title = "Start date of the tournament", 
#         description="for the project needs only allowed date format will be  'dd.mm.yyyy'",
#         max_length=10,
#         min_length=10,
#         example = "10.08.2022"
#         )
    
#     endDate: str = Field(
#         default=None,
#         title = "End date of the tournament", 
#         description="for the project needs only allowed date format will be  'dd.mm.yyyy'",
#         max_length=10,
#         min_length=10,
#         example = "10.08.2022"
#         )
    







# @app.get(path = "/tournaments/{tournament_id}")
# def retrieve_tournament(tournament_id: int = Path(title="Id of the tournament we want to get", ge=0)):
#     if len(fake_db) < tournament_id:
#         return fake_db[tournament_id]
#     else: 
#         return Response(status_code=404)

# @app.get(path = "/tournaments")
# def retrieve_tournaments(
#     name : str | None = None, 
#     tempo: TournamentTempo | None = None,
#     city : str | None = None,
#     countryState: CountryState | None = None,
#     tournamentState : TournamentState | None = None 
#   ):
#     return fake_db

# @app.post(path="/tournaments")
# def add_tournament(tournament : Tournament):
#     fake_db.append(tournament.__dict__)
#     return tournament