# logic/game_engine.py
# Core game logic: players, scores, rounds, bonus rules

from dataclasses import dataclass
from typing import List
from . import dice

@dataclass
class Player:
    name: str
    is_computer: bool = False
    score: int = 0

class GameEngine:
    def __init__(self, players: List[Player], total_rounds: int = 3):
        self.players = players
        self.total_rounds = total_rounds
        self.current_round = 1
        self.current_player_index = 0

    def reset(self):
        """Reset scores and round info."""
        for p in self.players:
            p.score = 0
        self.current_round = 1
        self.current_player_index = 0

    def get_current_player(self) -> Player:
        return self.players[self.current_player_index]

    def roll_turn(self):
        """
        Perform a turn for the current player.
        Bonus rule:
            - If player rolls a 6, they get an extra roll (unlimited until no 6).
        Returns:
            rolls (list[int]): all dice results for this turn
            turn_score (int): sum of all rolls
        """
        rolls = []
        while True:
            value = dice.roll_dice()
            rolls.append(value)
            if value != 6:     # stop extra rolls if no 6
                break

        turn_score = sum(rolls)
        player = self.get_current_player()
        player.score += turn_score
        return rolls, turn_score

    def next_player(self):
        """
        Move to the next player.
        After the last player of the round, move to next round.
        """
        self.current_player_index += 1
        if self.current_player_index >= len(self.players):
            self.current_player_index = 0
            self.current_round += 1

    def is_game_over(self) -> bool:
        """Game is over after all rounds are completed."""
        return self.current_round > self.total_rounds

    def get_winners(self) -> List[Player]:
        """Return list of winner(s) (to handle tie scores)."""
        max_score = max(p.score for p in self.players)
        return [p for p in self.players if p.score == max_score]
