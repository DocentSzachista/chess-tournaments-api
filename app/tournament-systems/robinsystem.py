
import json
import os 
from file_system_management import *


class RobinSystem: 
    
    def __init__(self, players : list, tournament_id : int ) -> None:
        self._players = players
        self._rounds = len(players) - 1
        self._current_round = 0
        self._tournament_id = tournament_id

    def generate_round(self):
        self._current_round += 1
        if self._rounds < self._current_round: 
            return "All rounds were generated"
        encounters = []
        
        pairs = len(self._players)//2   
        is_odd = len(self._players)%2 != 0 
 
        for i in range( pairs ) : 
            encounter = {
                "player_1" : self._players[i],
                "player_2" : self._players[-(i+1)],
                "score" : None
            }

            encounters.append( encounter )
        if self._current_round % 2 == 0:
            encounters[0]["player_1"], encounters[0]["player_2"] = encounters[0]["player_2"], encounters[0]["player_1"] 
        complete_encounters = encounters 
        

        if is_odd:
            complete_encounters["bye"] = self._players[pairs]

        swap = self._players.pop(len(self._players) -1)
        self._players.insert(1, swap)

        save_to_file(complete_encounters, self._tournament_id, self._current_round)
        return complete_encounters

    def apply_scores(self, round_numb : int, refreshed_encounters ): 
        save_to_file(refreshed_encounters, self._tournament_id, round_numb)

if __name__ == "__main__":
    players = [1, 2, 3, 4, 5, 6, 7, 8]
    # remove_dir("./", str(1))
    # create_dir("./", str(1) )
    robin = RobinSystem(players, 1)
    robin.generate_round()
    scores = load_round(1, 1)
    print(scores)
    scores[0]["score"] = 1 
    scores[1]["score"] = 2
    robin.apply_scores(1, scores)
    # list = []
    # for i in range(7):
    
    
    # print(robin.generate_round())