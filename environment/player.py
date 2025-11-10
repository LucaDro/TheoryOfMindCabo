class Player:
    def __init__(self, start_hand: list[int]) -> None:
        self.start_hand = start_hand
        self.known_hand = [self.start_hand[0], self.start_hand[1], -1, -1]