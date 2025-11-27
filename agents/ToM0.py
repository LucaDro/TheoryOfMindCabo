from player import Player

class ToM0(Player):
    def __init__(self, id, replace_limit, discard_limit, cabo_limit) -> None:
        """
        Args:
            id (_type_): player id
            replace_limit (_type_): replace an unknown card with a new card if new card is under this limit
            cabo_limit (_type_): call cabo if total points is under this limit
        """
        self.replace_limit = replace_limit
        self.discard_limit = discard_limit
        self.cabo_limit = cabo_limit
        super().__init__(id)

    def card_total(self, player_id) -> int:
        sum = 0
        for card in self.known_cards[player_id]:
            if card == -1:
                return -1
            elif card != -2:
                sum += card
        return sum

    def choose_drawpile(self, discard_value: int) -> int:
        """chooses wether to draw a card from draw pile or discard pile or to call Cabo.
        If the total sum of cards is under the cabo limit, call cabo (2)
        If the value of the card on the discard pile is less than the discard limit and smaller than the largest card you have -1, or if you have an unknown card in your hand, draw from discard pile (1)
        Any other case, draw from the draw pile (0)

        Args:
            discard_value (int): value of the top card on the discard pile

        returns:
            int: 0 if player draws from draw pile, 1 if player draws from discard pile and 2 if player calls Cabo
        """
        total = self.card_total(self.id)
        if total != -1 and total < self.cabo_limit:
            return 2
        if discard_value < self.discard_limit and (discard_value < (max(self.known_cards[self.id])-1) or (-1 in self.known_cards[self.id])):
            return 1
        else:
            return 0
        
    def choose_action(self, card_value: int) -> int:
        """chooses which action to take given the value of the card picked up
        swaps it with one of own cards if one of the cards is unknown, or the card is lower than the highest card
        discards it in all other cases

        Args:
            card_value (int): value of the picked up card

        Returns:
            int: action to take, 0 to swap, 1 to discard
        """
        if card_value < max(self.known_cards[self.id]):
            return 0
        if -1 in self.known_cards[self.id]:
            return 0
        return 1
    
    def choose_swap(self, card_value: int) -> int:
        if -1 in self.known_cards[self.id]:
            return self.known_cards[self.id].index(-1)
        else:
            max_value = max(self.known_cards[self.id])
            return self.known_cards[self.id].index(max_value)
        
    def choose_use_special(self, card_value: int) -> int:
        if card_value == 7 or card_value == 8:
            if -1 in self.known_cards[self.id]:
                return 1
            return 0
        if card_value == 9 or card_value == 10:
            if -1 in self.known_cards[(self.id + 1) % 2]:
                return 1
            return 0
        if card_value == 11 or card_value == 12:
            for card in self.known_cards[(self.id+1)%2]:
                if card != -1 and (card < max(self.known_cards[self.id]) or (-1 in self.known_cards[self.id])):
                    return 1
            return 0
        
    def choose_peek_special(self) -> int:
        for index, card in enumerate(self.known_cards[self.id]):
            if card == -1:
                return index
        return 0
    
    def choose_spy_special(self) -> int:
        for index, card in enumerate(self.known_cards[(self.id+1)%2]):
            if card == -1:
                return index
        return 0
    
    def choose_swap_special(self) -> tuple[int, int]:
        if -1 in self.known_cards[self.id]:
            player_index = self.known_cards[self.id].index(-1)
        else:
            max_value = max(self.known_cards[self.id])
            player_index = self.known_cards[self.id].index(max_value)
        max_opponent_value = max(self.known_cards[(self.id+1)%2])
        opponent_index = self.known_cards[(self.id+1)%2].index(max_opponent_value)
        return player_index, opponent_index