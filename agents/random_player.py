from agents.player import Player
from random import Random

class Random_player(Player):
    """
    Player that picks actions randomly, they cannot call Cabo
    """
    def __init__(self, id) -> None:
        self.random = Random()
        super().__init__(id)

    def choose_drawpile(self, discard_value: int) -> int:
        return self.random.randint(0,1)
    
    def choose_action(self, card_value: int) -> int:
        return self.random.randint(0,1)
    
    def choose_swap(self, card_value: int) -> int:
        return self.random.randint(0,3)
    
    def choose_use_special(self, card_value: int) -> int:
        return self.random.randint(0,1)
    
    def choose_peek_special(self) -> int:
        return self.random.randint(0,3)
    
    def choose_spy_special(self) -> int:
        return self.random.randint(0,3)
    
    def choose_swap_special(self) -> tuple[int, int]:
        player_index = self.random.randint(0,3)
        opponent_index = self.random.randint(0,3)
        return player_index, opponent_index
    