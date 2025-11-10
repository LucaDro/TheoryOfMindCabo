class Discard:
    def __init__(self, topcard) -> None:
        self.topcard = topcard

    def draw(self) -> int:
        return self.topcard
    
    def discard(self, card: int) -> None:
        self.topcard = card