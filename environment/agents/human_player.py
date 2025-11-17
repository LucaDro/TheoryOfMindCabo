from player import Player

class Human(Player):
    def player_announcement(self):
        print("you are player ", self.id)

    def print_known_hands(self):
        print("your hand: ", end = "")
        for i in range(4):
            print(self.known_cards[self.id][i], end = " ")
        print("")
        print("opponent's hand: ", end = "")
        for i in range(4):
            print(self.known_cards[(self.id+1)%2][i], end = " ")
        print("")

    def choose_drawpile(self, card_value: int) -> int:
        print("")
        self.player_announcement()
        self.print_known_hands()
        print("the card on the discard pile is: ", card_value)
        print("choose 0 to pick from draw pile")
        print("Choose 1 to pick from discard pile")
        print("Choose 2 to call Cabo: 2")
        pile = int(input())
        while pile < 0 or pile > 2:
            print("Not a valid choice")
            pile = int(input())
        return pile

    def choose_action(self, card_value: int) -> int:
        print("")
        self.print_known_hands()
        print("The card you have in picked up is: ", card_value)
        print("Choose 0 to swap with one of your cards")
        print("Choose 1 to discard the card")
        action = int(input())
        while action < 0 or action > 1:
            print("Not a valid choice")
            action = int(input())
        return action
    
    def choose_swap(self, card_value: int) -> int:
        print("")
        print("The card you have in picked up is: ", card_value)
        print("Choose which card index to swap this card with (from 0-3)")
        index = int(input())
        while index < 0 or index > 3:
            print("Not a valid choice")
            index = int(input())
        return index

    def choose_use_special(self, card_value: int) -> int:
        print("")
        print("Would you like to use the power of this card? 7 and 8 is peek, 9 and 10 is spy, 11 and 12 is swap")
        print("0 if no, 1 if yes")
        use = int(input())
        while use < 0 or use > 1:
            print("Not a valid option")
            use = int(input())
        return use
    
    def choose_peek_special(self) -> int:
        print("")
        print("Which card would you like to peek at from your own hand? Give card index (from 0-3)")
        index = int(input())
        while index < 0 or index > 3:
            print("Not a valid choice")
            index = int(input())
        return index
    
    def choose_spy_special(self) -> int:
        print("")
        print("Which card would you like to spy at from your opponent's hand? Give card index (from 0-3)")
        index = int(input())
        while index < 0 or index > 3:
            print("Not a valid choice")
            index = int(input())
        return index
    
    def choose_swap_special(self) -> tuple[int, int]:
        print("")
        print("Which of your cards would you like to swap with from your own hand? Give card index (from 0-3)")
        player_card = int(input())
        while player_card < 0 or player_card > 3:
            print("Not a valid choice")
            player_card = int(input())
        print("Which of your cards would you like to swap with from your opponent's hand? Give card index (from 0-3)")
        opponent_card = int(input())
        while opponent_card < 0 or opponent_card > 3:
            print("Not a valid choice")
            opponent_card = int(input())
        return player_card, opponent_card