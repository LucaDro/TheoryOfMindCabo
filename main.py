from environment.game import Game
from environment.deck import Deck
from agents.human_player import Human
from agents.random_player import Random_player
from agents.ToM0 import ToM0

game = Game()

win_rate = [0,0,0]

player_1 = Random_player(0)
player_2 = ToM0(1, 8, 4, 5)

for i in range(100000):
    deck = Deck()
    game.new_game(player_1, player_2, deck)
    winner = game.start_game()
    if winner != -1:
        win_rate[winner] += 1
    else:
        win_rate[2] += 1

print("player 1 won ", win_rate[0], " rounds")
print("player 2 won ", win_rate[1], " rounds")
print(win_rate[2], " rounds ended in ties")
