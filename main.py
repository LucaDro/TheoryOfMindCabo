from environment.game import Game
from agents.human_player import Human
from agents.random_player import Random_player
from agents.ToM0 import ToM0

game = Game()

player_0 = Human(0)
player_1 = ToM0(1, 6, 4, 5)

game.new_game(player_0, player_1)
winner = game.start_game()

print("The winner is Player ", winner)
