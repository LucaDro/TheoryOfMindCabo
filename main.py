from environment.game import Game
from agents.human_player import Human

game = Game()

player_0 = Human(0)
player_1 = Human(1)

game.new_game(player_0, player_1)
winner = game.start_game()

print("The winner is Player ", winner)
