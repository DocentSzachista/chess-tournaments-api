from doctest import Example
from pydantic import BaseModel, Field
from .enums import TournamentTempo, CountryState

class TournamentBase(BaseModel): 
    name: str = Field(
        title = "The title of tournament", 
        description = "Remember to not exceed its max lenght", 
        max_length = 150,
        example = "chess international 2022 in Wroclaw"
        ) 
    
    city: str = Field(
        title = "City of the tournament", 
        max_length = 50,
        example = "Wrocław" 
        )
    
    startDate: str = Field(
        title = "Start date of the tournament", 
        description="for the project needs only allowed date format will be  'dd.mm.yyyy'",
        max_length=10,
        min_length=10,
        example = "10.08.2022"
        )
    
    tempo: TournamentTempo = Field(
        default=None, 
        title="tournament tempo", 
        description="You must provide one of given types",
        example = TournamentTempo.classic
        )

    endDate: str = Field(
        default=None,
        title = "End date of the tournament", 
        description="for the project needs only allowed date format will be  'dd.mm.yyyy'",
        max_length=10,
        min_length=10,
        example = "10.08.2022"
        )

class TournamentDB(TournamentBase): 
    address: str = Field(
        title = "Address of a building where tournament takes place",
        max_length=255,
        example = "Krajowa 8"
    )
    roundsNumber : int = Field(
        title="number of rounds in tournament",
        example = 7
    )
    system: str = Field(
        title="System in which people are divided into pairs",
        example = "Swiss"        
    )
    countryState: CountryState = Field( 
        default = None, 
        title = "contains info about in which country state tournament takes part",
        example = CountryState.DS 
        )
class TournamentOut(TournamentBase): 
    id: int 
    class Config: 
        orm_mode = True