from enum import Enum

class TournamentTempo(str, Enum):
    empty = ""
    blitz = "blitz"
    rapid = "rapid"
    classic = "classic"

class CountryState(str, Enum):
    empty = ""
    DS = "DS"
    LB = "LB"
    WM = "WM"

class TournamentState(str, Enum):
    planned = "planned"
    ongoing = "ongoing"
    finished = "finished"

class Gender(str, Enum):
    man = "M"
    woman = "W"