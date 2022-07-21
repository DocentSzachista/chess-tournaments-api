
import json
import os 
from file_system_management import *


class RobinSystem: 
    
    # def __init__(self, players : list, tournament_id : int ) -> None:
    #     self._players = players
    #     self._rounds = len(players) - 1
    #     self._current_round = 0
    #     self._tournament_id = tournament_id
    # @staticmethod
    def generate_round(self, current_round, players, tournament_id ):
      
        if current_round > 1:
            for i in range(current_round):
                swap = players.pop(len(players) -1)
                players.insert(1, swap)
        encounters = []
        
        pairs = len(players)//2   
        is_odd = len(players)%2 != 0 
 
        for i in range( pairs ) : 
            encounter = {
                "player_1" : players[i],
                "player_2" : players[-(i+1)],
                "score" : None
            }

            encounters.append( encounter )
        if current_round % 2 == 0:
            encounters[0]["player_1"], encounters[0]["player_2"] = encounters[0]["player_2"], encounters[0]["player_1"] 
        complete_encounters = encounters 
        

        if is_odd:
            complete_encounters["bye"] = players[pairs]

        

        save_to_file(complete_encounters, tournament_id, current_round)
        return complete_encounters
    
    def apply_scores(self, round_numb : int, tournament_id: int, refreshed_encounters: list ): 
        save_to_file(refreshed_encounters, tournament_id, round_numb)

