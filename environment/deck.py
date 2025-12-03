from random import shuffle;

DEFAULT_DECK = [0,0,
                1,1,1,1,
                2,2,2,2,
                3,3,3,3,
                4,4,4,4,
                5,5,5,5,
                6,6,6,6,
                7,7,7,7,
                8,8,8,8,
                9,9,9,9,
                10,10,10,10,
                11,11,11,11,
                12,12,12,12,
                13,13]

class Deck:
    def __init__(self) -> None:
        self.cards = DEFAULT_DECK.copy()

    def shuffle(self) -> None:
        shuffle(self.cards)

    def draw(self) -> int:
        card = self.cards.pop(0)
        return card
    
    def empty(self) -> bool:
        # print(len(self.cards))
        if len(self.cards) == 0:
            return True
        else:
            return False
    
    def reset(self) -> None:
        self.cards = DEFAULT_DECK