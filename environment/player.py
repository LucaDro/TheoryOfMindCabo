class Player:
    """
    Abstract class for player
    """
    def __init__(self, id) -> None:
        self.id = id
        self.known_cards = [[-1,-1,-1,-1],[-1,-1,-1,-1]]

    def learn_card(self, player_id: int, card_index: int, card_value: int) -> None:
        self.known_cards[player_id][card_index] = card_value
        return

    def choose_drawpile(self, discard_value: int) -> int:
        """chooses wether to draw a card from draw pile or discard pile or to call Cabo.

        Args:
            discard_value (int): value of the top card on the discard pile

        returns:
            int: 0 if player draws from draw pile, 1 if player draws from discard pile and 2 if player calls Cabo
        """
        pass

    def choose_action(self, card_value: int) -> int:
        """chooses which action to take given the value of the card picked up

        Args:
            card_value (int): value of the picked up card

        Returns:
            int: action to take, 0 to swap, 1 to discard, 2 to use special power
            on card (if applicable)
        """
        pass

    def choose_swap(self, card_value: int) -> int:
        """Chooses which of the cards in the players hand to swap the picked up card with
        updates their own known hands and returns the index of the card

        Args:
            card_value (int): value of the picked up card

        Returns:
            int: index of which card to swap with
        """
        pass

    def choose_peek_special(self) -> int:
        """Chooses which card to look at in their own hand

        Returns:
            int: index of the card they peek at in their own hand
        """
        pass

    def choose_spy_special(self) -> int:
        """Chooses which card to look at in their opponents hand

        Returns:
            int: index of the card they peek at in their opponents hand
        """
        pass

    def choose_swap_special(self) -> tuple(int):
        """Chooses two cards to swap, one from their hand and one from their opponents hand

        Returns:
            int: indexes of cards, first the one they are swapping from their hand and
            second the one they are swapping with
        """
        pass

    def throw_away(self, card_value: int) -> list[int]:
        """Checks if players have a card of the same value as the one that was just placed
        on the discard and throws that card away if they do

        Args:
            card_value (int): the value of the card that was just placed on the discard

        Returns:
            list[int]: list of the indexes of the cards from the players hand that have the same value 
            as the card that was just discarded. If there are no same cards, the list is empty
        """
        same_value: list[int] = []
        for i in range(4):
            if self.known_cards[self.id][i] == card_value:
                same_value.append(i)
                self.known_cards[self.id][i] = -2
        return same_value
