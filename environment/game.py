from environment.deck import Deck
from agents.player import Player

class Game:
    def __init__(self) -> None:
        pass

    def new_game(self, player_0: Player, player_1: Player, deck: Deck) -> None:
        self.draw_pile: Deck = deck
        self.draw_pile.shuffle()
        self.discard = self.draw_pile.draw()
        self.players: list[Player] = [player_0, player_1]
        self.player_cards = [[0, 0, 0, 0],[0, 0, 0, 0]]
        for i in range(2):
            for j in range(4):
                self.player_cards[i][j] = self.draw_pile.draw()
        for i in range(2):
            for j in range(2):
                self.players[i].learn_card(i, j, self.player_cards[i][j])

    def start_game(self) -> int:
        start_player = 0
        next_turn = self.player_turn(start_player)
        while next_turn:
            start_player = (start_player+1)%2
            next_turn = self.player_turn(start_player)
            if self.draw_pile.empty():
                return self.end_game()
            flag = 1
            for i in range(4):
                if self.player_cards[0][i] != -1:
                    flag = 0
                    break
            if flag == 1:
                return 0
            flag = 1
            for i in range(4):
                if self.player_cards[1][i] != -1:
                    flag = 0
                    break
            if flag == 1:
                return 1
        start_player = (start_player+1)%2
        self.player_turn(start_player)
        return self.end_game()
    
    def special_move(self, chosen_card, player_id):
        current_player: Player = self.players[player_id]
        opposing_player: Player = self.players[(player_id + 1)%2]
        if (chosen_card + 1) // 2 == 4:
            index = current_player.choose_peek_special()
            while index < 0 or index > 3 or self.player_cards[player_id][index] == -1:
                # print("not an option, choose again")
                index = current_player.choose_peek_special()
            current_player.learn_card(player_id, index, self.player_cards[player_id][index])
        if (chosen_card + 1) // 2 == 5:
            index = current_player.choose_spy_special()
            while index < 0 or index > 3 or self.player_cards[(player_id+1)%2][index] == -1:
                # print("not an option, choose again")
                index = current_player.choose_spy_special()
            current_player.learn_card((player_id+1)%2, index, self.player_cards[(player_id+1)%2][index])
        if (chosen_card + 1) // 2 == 6:
            player_index, opponent_index = current_player.choose_swap_special()
            while player_index < 0 or player_index > 3 and self.player_cards[player_index][index] == -1 or opponent_index < 0 or opponent_index > 3 and self.player_cards[(player_id + 1)%2][opponent_index]:
                # print("not an option, choose again")
                index = current_player.choose_spy_special()
            # Values of the swapped cards according to the players' knowledge
            swapped_player_card_player_knowledge = current_player.known_cards[player_id][player_index]
            swapped_opponent_card_player_knowledge = current_player.known_cards[(player_id + 1)%2][opponent_index]
            swapped_player_card_opponent_knowledge = opposing_player.known_cards[player_id][player_index]
            swapped_opponent_card_opponent_knowedge = opposing_player.known_cards[(player_id + 1)%2][opponent_index]
            # Swapping the cards in the players' knowledge base
            current_player.learn_card(player_id, player_index, swapped_opponent_card_player_knowledge)
            current_player.learn_card((player_id + 1)%2, opponent_index, swapped_player_card_player_knowledge)
            opposing_player.learn_card(player_id, player_index, swapped_opponent_card_opponent_knowedge)
            opposing_player.learn_card((player_id + 1)%2, opponent_index, swapped_player_card_opponent_knowledge)
            # Swaps the cards in the game managers knowledge
            self.player_cards[player_id][player_index], self.player_cards[(player_id + 1)%2][opponent_index] = self.player_cards[(player_id + 1)%2][opponent_index], self.player_cards[player_id][player_index]

            
    def player_turn(self, player_id: int) -> int:
        # print("")
        # print("GOD MODE")
        # print("discard: ", self.discard)
        # for i in range(2):
        #     for j in range(4):
        #         print(self.player_cards[i][j], end = " ")
        #     print("")
        # print("")
        current_player: Player = self.players[player_id]
        opposing_player: Player = self.players[(player_id+1)%2]
        chosen_pile: int = current_player.choose_drawpile(self.discard)
        while chosen_pile < 0 or chosen_pile > 2:
            # print("not an option, choose again")
            chosen_pile = current_player.choose_drawpile(self.discard)
        # Pile chosen is discard
        if chosen_pile ==  1:
            chosen_card = self.discard
            index = current_player.choose_swap(chosen_card)
            while index < 0 or index > 3 or self.player_cards[player_id][index] == -1:
                # print("not an option, choose again")
                index = current_player.choose_swap(chosen_card)
            discard_card = self.player_cards[player_id][index]
            self.player_cards[player_id][index] = chosen_card
            current_player.learn_card(player_id, index, chosen_card)
            opposing_player.learn_card(player_id, index, chosen_card)
        # Player called Cabo
        elif chosen_pile == 2:
            return 0
        # Pile chosen is draw pile
        else:
            chosen_card = self.draw_pile.draw()
            action = current_player.choose_action(chosen_card)
            if action < 0 or action > 1:
                # print("not an option, choose again")
                action = current_player.choose_action(chosen_card)
            # Action chosen is to swap card with one of their own cards
            if action == 0:
                index = current_player.choose_swap(chosen_card)
                while index < 0 or index > 3 or self.player_cards[player_id][index] == -1:
                    # print("not an option, choose again")
                    index = current_player.choose_swap(chosen_card)
                discard_card = self.player_cards[player_id][index]
                self.player_cards[player_id][index] = chosen_card
                current_player.learn_card(player_id, index, chosen_card)
                opposing_player.learn_card(player_id, index, -1)
            # Action chosen is to discard the card
            elif action == 1:
                discard_card = chosen_card
        if discard_card >= 7 and discard_card <= 12:
            if current_player.choose_use_special(discard_card):
                self.special_move(discard_card, current_player.id)
        self.discard = discard_card
        # Players can throw away cards if they are of the same value as discarded card this turn
        for player in self.players:
            thrown_away = player.throw_away(self.discard)
            for card in thrown_away:
                self.player_cards[player.id][card] = -1
                for inform_player in self.players:
                    inform_player.learn_card(player.id, card, -2)
        return 1

    def end_game(self) -> int:
        """Counts up the points and returns the winner's player id

        Returns:
            int: The ID of the winner of the game or -1 if it's a tie
        """
        player_score = [0,0]
        for player in self.players:
            id = player.id
            for i in range(4):
                if self.player_cards[id][i] != -1:
                    player_score[id] += self.player_cards[id][i]
        if player_score[0] > player_score[1]:
            return 1
        elif player_score[0] < player_score[1]:
            return 0
        else:
            return -1
