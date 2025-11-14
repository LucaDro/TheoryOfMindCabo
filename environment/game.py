from deck import Deck
from discard import Discard
from player import Player

class Game:
    def __init__(self) -> None:
        pass

    def new_game(self) -> None:
        self.draw_pile: Deck = Deck()
        self.draw_pile.shuffle()
        self.discard = self.draw_pile.draw()
        player_0: Player = Player(0)
        player_1: Player = Player(1)
        self.players: list[Player] = [player_0, player_1]
        self.player_cards = [[],[]]
        for i in range(2):
            for j in range(4):
                self.player_cards[i][j] = self.draw_pile.draw()
        for i in range(2):
            for j in range(2):
                self.players[i].learn_card(i, j, self.player_cards[i][j])

    def start_game(self) -> None:
        pass

    def player_turn(self, player_id: int) -> None:
        current_player: Player = self.players[player_id]
        opposing_player: Player = self.players[(player_id+1)%2]
        chosen_pile: int = current_player.choose_drawpile(self.discard)
        if chosen_pile:
            chosen_card = self.discard
            index = current_player.choose_swap(chosen_card)
            self.player_cards[player_id][index] = chosen_card
            opposing_player.learn_card(player_id, index, chosen_card)
        else:
            chosen_card = self.draw_pile.draw()
            action = current_player.choose_action(chosen_card)
            if action == 0:
                index = current_player.choose_swap(chosen_card)
                self.player_cards[player_id][index] = chosen_card
            elif action == 1:
                pass
            else:
                if (chosen_card + 1) // 2 == 4:
                    index = current_player.choose_peek_special()
                    current_player.learn_card(player_id, index, self.player_cards[player_id][index])
                if (chosen_card + 1) // 2 == 5:
                    index = current_player.choose_spy_special()
                    current_player.learn_card((player_id+1)%2, index, self.player_cards[(player_id+1)%2][index])
                if (chosen_card + 1) // 2 == 6:
                    player_index, opponent_index = current_player.choose_swap_special()
                    # Values of the swapped cards according to the players' knowledge
                    swapped_player_card_player_knowledge = current_player.known_cards[player_id][player_index]
                    swapped_opponent_card_player_knowledge = current_player.known_cards[(player_id + 1)%2][opponent_index]
                    swapped_player_card_opponent_knowledge = opposing_player.known_cards[player_id][player_index]
                    swapped_opponent_card_opponent_knowedge = opposing_player.known_cards[(player_id + 1)%2][opponent_index]
                    # Swapping the cards in the players' knowledge base
                    current_player.learn_card(player_id, player_index, swapped_opponent_card_player_knowledge)
                    current_player.learn_card((player_id + 1)%2, opponent_index, swapped_player_card_player_knowledge)
                    opposing_player.learn_card(player_id, player_index, swapped_opponent_card_opponent_knowedge)
                    current_player.learn_card((player_id + 1)%2, opponent_index, swapped_player_card_opponent_knowledge)
                    # Swaps the cards in the game managers knowledge
                    self.player_cards[player_id][player_index], self.player_cards[(player_id + 1)%2][opponent_index] = self.player_cards[(player_id + 1)%2][opponent_index], self.player_cards[player_id][player_index]
            self.discard = chosen_card
            for player in self.players:
                thrown_away = player.throw_away(self.discard)
                for card in thrown_away:
                    self.player_cards[player.id][card] = -1

                    
