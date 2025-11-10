from deck import Deck
from discard import Discard
from player import Player

class Game:
    def __init__(self) -> None:
        self.new_game
        
    def new_game(self) -> None:
        deck = Deck()
        deck.shuffle()
        discard = Discard(deck.draw())
        player1_hand = []
        for i in range(4):
            player1_hand.append(deck.draw())
        player2_hand = []
        for i in range(4):
            player2_hand.append(deck.draw())
        player1 = Player(player1_hand)
        player2 = Player(player2_hand)